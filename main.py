from flask import Flask
from src.models import db


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = (
        "2fd3f4ccbade3edb9bc2efd0bc6bfbe7a4b6ae8b0c0bc0a3928ce7275ded27ff"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

    db.init_app(app)

    from src.routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
