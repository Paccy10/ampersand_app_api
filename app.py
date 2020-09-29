""" Main application module """

from flask import Flask, Blueprint
from flask_migrate import Migrate


from config.server import application
from config.db import db
from api.utils.helpers.response import Response
from api.models.motocycle import Motocycle
import api.views.motocycle

Migrate(application, db)


@application.route('/', methods=['GET'])
def home():
    """ Home route """

    return Response.success('Welcome to Ampersand API', None, 200)


@application.errorhandler(404)
def page_not_found(error):
    """ Undefined route handler """

    return Response.error('Route Not found', 404)


if __name__ == '__main__':
    application.run()
