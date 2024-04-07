from flask import Flask, render_template, url_for, request, redirect, flash  # noqa: F401
from form import RegistrationForm, LoginForm


app = Flask(__name__)

app.config["SECRET_KEY"] = (
    "2fd3f4ccbade3edb9bc2efd0bc6bfbe7a4b6ae8b0c0bc0a3928ce7275ded27ff"
)

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


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Flask Blog")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(
            url_for("home")
        )  # Redirect to login page after successful registration
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))  # Redirect to home after successful login
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
