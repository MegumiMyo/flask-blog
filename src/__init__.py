import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Load environment variables from .env file
load_dotenv()


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Configure Flask-Login settings
    login_manager.login_view = (
        "main.login"  # Specify login view for unauthorized access redirection
    )
    login_manager.login_message_category = (
        "info"  # Set flash message category for login messages
    )

    from src.routes import bp

    app.register_blueprint(bp)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app


# def create_app():
#     app = Flask(__name__)

#     # Load configuration from environment variables
#     app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
#     app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#     # Initialize Flask extensions with the Flask app
#     db.init_app(app)
#     bcrypt.init_app(app)
#     login_manager.init_app(app)

#     # Configure Flask-Login settings
#     login_manager.login_view = (
#         "main.login"  # Specify login view for unauthorized access redirection
#     )
#     login_manager.login_message_category = (
#         "info"  # Set flash message category for login messages
#     )

#     # Register the main blueprint for routing
#     app.register_blueprint(bp)

#     # Create database tables if they don't exist
#     with app.app_context():
#     db.create_all()

# return app
