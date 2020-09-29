""" Module for Motocycle Model """

from config.db import db
from .base import BaseModel


class Motocycle(BaseModel):
    """ Motocycle Model class """

    __tablename__ = 'motocycles'

    serial_number = db.Column(db.String(100), nullable=False, unique=True)
    odometer = db.Column(db.Float, nullable=False, default=0.00)
