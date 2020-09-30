""" Module for the Battery Schema """

from marshmallow import fields

from .base import BaseSchema


class BatterySchema(BaseSchema):
    """ Battery Schema Class """

    serial_number = fields.String(required=True)
    capacity = fields.Float(required=True)
    energy_level = fields.Float(required=True)
