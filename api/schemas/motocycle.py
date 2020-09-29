""" Module for the Motocycle Schema """

from marshmallow import fields

from .base import BaseSchema


class MotocycleSchema(BaseSchema):
    """ Motocycle Schema Class """

    serial_number = fields.String(required=True)
    odometer = fields.Float(required=True)
