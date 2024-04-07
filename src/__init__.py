from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = (
    "2fd3f4ccbade3edb9bc2efd0bc6bfbe7a4b6ae8b0c0bc0a3928ce7275ded27ff"
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from src import routes  # noqa: E402, F401
