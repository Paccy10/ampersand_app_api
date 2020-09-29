""" Module for Server configuration """

from flask import Flask, Blueprint
from flask_migrate import Migrate

from .env import AppConfig


def create_app(config=AppConfig):
    """ Create the flask application """

    app = Flask(__name__)
    app.config.from_object(config)

    return app


application = create_app()
