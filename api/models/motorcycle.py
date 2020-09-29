""" Module for Motorcycle Model """

from config.db import db
from .base import BaseModel


class Motorcycle(BaseModel):
    """ Motorcycle Model class """

    __tablename__ = 'motorcycles'

    serial_number = db.Column(db.String(100), nullable=False, unique=True)
    odometer = db.Column(db.Float, nullable=False, default=0.00)
