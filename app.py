""" Main application module """

from flask import Flask, Blueprint

from config.env import AppConfig
from api.utils.helpers.response import Response

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')


def create_app(config=AppConfig):
    """ Create the flask application """

    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(api_blueprint)

    return app


application = create_app()


@application.errorhandler(404)
def page_not_found(error):
    """ Undefined route handler """

    return Response.error('Route Not found', 404)


if __name__ == '__main__':
    application.run()
