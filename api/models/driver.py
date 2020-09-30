""" Module for Driver Model """

from config.db import db
from .base import BaseModel


class Driver(BaseModel):
    """ Driver Model class """

    __tablename__ = 'drivers'

    name = db.Column(db.String(250), nullable=False, unique=True)
    license_number = db.Column(db.String(100), nullable=False, unique=True)
    motorcycle_id = db.Column(db.Integer, db.ForeignKey(
        'motorcycles.id'), nullable=False)
    motorcycle = db.relationship(
        'Motorcycle', backref='driver_motorcycle', lazy='joined')
