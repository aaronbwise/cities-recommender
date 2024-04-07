from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret"

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
