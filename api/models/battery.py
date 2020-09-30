""" Module for Battery Model """

from config.db import db
from .base import BaseModel


class Battery(BaseModel):
    """ Battery Model class """

    __tablename__ = 'batteries'

    serial_number = db.Column(db.String(100), nullable=False, unique=True)
    capacity = db.Column(db.Float, nullable=False, default=0.00)
