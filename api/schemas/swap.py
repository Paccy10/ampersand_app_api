""" Module for the Swap Schema """

from marshmallow import fields

from .base import BaseSchema
from .driver import DriverSchema
from .station import StationSchema


class SwapSchema(BaseSchema):
    """ Swap Schema Class """

    driver = fields.Nested(DriverSchema(
        only=('name', 'license_number', 'motorcycle')))
    station = fields.Nested(StationSchema(
        only=('location', 'number_of_batteries',)))
    old_battery = fields.Dict(required=True)
    new_battery = fields.Dict(required=True)
    distance_covered = fields.Float(required=True)
    energy_used = fields.Float(required=True)
