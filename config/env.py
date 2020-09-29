""" Module for the application environments configurations """

from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """ App base configurations """

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """ App Development configurations """

    PORT = 5000
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')


class ProductionConfig(Config):
    """ App production configurations """

    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

AppConfig = config.get(getenv('FLASK_ENV'))
