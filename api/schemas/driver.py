""" Module for the Driver Schema """

from marshmallow import fields

from .base import BaseSchema
from .motorcycle import MotorcycleSchema


class DriverSchema(BaseSchema):
    """ Driver Schema Class """

    name = fields.String(required=True)
    license_number = fields.String(required=True)
    motorcycle = fields.Nested(MotorcycleSchema(only=('id', 'serial_number')))
