from flask import render_template, url_for, redirect, flash, Blueprint
from src.form import RegistrationForm, LoginForm
from src.models import User, Post  # noqa: F401

bp = Blueprint("main", __name__)

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    },
]


@bp.route("/")
@bp.route("/home")
def home():
    # posts = Post.query.all()
    return render_template("home.html", posts=posts, title="Flask Blog")


@bp.route("/about")
def about():
    return render_template("about.html", title="About")


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)
