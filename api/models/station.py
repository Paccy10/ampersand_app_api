""" Module for Station Model """

from config.db import db
from .base import BaseModel


class Station(BaseModel):
    """ Station Model class """

    __tablename__ = 'stations'

    location = db.Column(db.String(250), nullable=False, unique=True)
    number_of_batteries = db.Column(
        db.Integer, nullable=False, unique=True)
