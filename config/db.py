""" Module for initiliazing the database """

from flask_sqlalchemy import SQLAlchemy

from .server import application

db = SQLAlchemy(application)
