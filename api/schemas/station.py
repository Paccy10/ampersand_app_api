""" Module for the Station Schema """

from marshmallow import fields

from .base import BaseSchema
from .motorcycle import MotorcycleSchema


class StationSchema(BaseSchema):
    """ Station Schema Class """

    location = fields.String(required=True)
    number_of_batteries = fields.Integer(required=True)
