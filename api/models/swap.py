""" Module for Swap Model """

from sqlalchemy.dialects.postgresql import JSON

from config.db import db
from .base import BaseModel


class Swap(BaseModel):
    """ Swap Model class """

    __tablename__ = 'swaps'

    driver_id = db.Column(db.Integer, db.ForeignKey(
        'drivers.id'), nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey(
        'stations.id'), nullable=False)
    old_battery = db.Column(JSON, nullable=False)
    new_battery = db.Column(JSON, nullable=False)
    distance_covered = db.Column(db.Float, nullable=False)
    energy_used = db.Column(db.Float, nullable=False)

    driver = db.relationship(
        'Driver', backref='swap_driver', lazy='joined')
    station = db.relationship(
        'Station', backref='swap_station', lazy='joined')
