import os
import secrets
from PIL import Image
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
    abort,
)
from flask_login import login_user, current_user, logout_user, login_required
from src.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from src import db, bcrypt
from src.models import User, Post

bp = Blueprint("main", __name__)


@bp.route("/")
@bp.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts, title="Flask Blog")


@bp.route("/about")
def about():
    return render_template("about.html", title="About")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You can now log in.", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", title="Register", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            # flash("Login successful!", "success")
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash("Login unsuccessful. Please check your email and password.", "danger")
    return render_template("login.html", title="Login", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(bp.root_path, "static", "images")

    if not os.path.exists(picture_path):
        os.makedirs(picture_path)

    picture_path = os.path.join(picture_path, picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@bp.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():  # Correctly call form.validate_on_submit()
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("main.account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for(
        "static", filename="images/" + current_user.image_file
    )  # Correct image file path
    return render_template(
        "account.html", title="Account", image_file=image_file, form=form
    )


@bp.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user,
        )
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", "success")
        return redirect(url_for("main.home"))
    return render_template(
        "create_post.html", title="New Post", form=form, legend="Add Post"
    )


@bp.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post.title, post=post)


@bp.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated!", "success")
        return redirect(url_for("main.post", post_id=post.id))

    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content

    return render_template(
        "edit_post.html", title="Update Post", form=form, legend="Update Post"
    )


@bp.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("main.home"))


@bp.route("/post/<string:username>")
def user_posts(username):
    page = request.args.get("page", 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = (
        Post.query.filter_by(author=user)
        .order_by(Post.date_posted.desc())
        .paginate(page=page, per_page=5)
    )
    return render_template("user_post.html", posts=posts, user=user)
