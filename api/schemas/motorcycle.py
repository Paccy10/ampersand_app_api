""" Module for the Motorcycle Schema """

from marshmallow import fields

from .base import BaseSchema


class MotorcycleSchema(BaseSchema):
    """ Motorcycle Schema Class """

    serial_number = fields.String(required=True)
    odometer = fields.Float(required=True)
