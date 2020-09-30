""" Module for motorcycles endpoints """

from flask import request

from config.server import application
from ..models.motorcycle import Motorcycle
from ..schemas.motorcycle import MotorcycleSchema
from ..utils.helpers.response import Response
from ..utils.helpers.messages import (MOTORCYCLE_CREATED,
                                      KEY_REQUIRED,
                                      MOTORCYCLE_EXISTS,
                                      MOTORCYCLES_FETCHED)
from ..utils.helpers import request_data_strip


@application.route('/motorcycles', methods=['POST'])
def create_motorcycle():
    """ Endpoint to create the motorcycle """

    request_data = request.get_json()
    if not request_data.get('serial_number') or not request_data.get('serial_number').strip():
        return Response.error(KEY_REQUIRED.format('serial_number'), 400)

    motorcycle = Motorcycle.query.filter(
        Motorcycle.serial_number == request_data.get('serial_number').strip()).first()
    if motorcycle:
        return Response.error(MOTORCYCLE_EXISTS, 409)

    new_motorcycle = Motorcycle(**request_data_strip(request_data))
    new_motorcycle.save()
    motorcycle_schema = MotorcycleSchema()
    response_data = {
        'motorcycle': motorcycle_schema.dump(new_motorcycle)
    }
    return Response.success(MOTORCYCLE_CREATED, response_data, 201)


@application.route('/motorcycles', methods=['GET'])
def get_motorcycles():
    """ Endpoint to get the motorcycles """

    motorcycles = Motorcycle.query.all()

    motorcycle_schema = MotorcycleSchema(many=True)
    response_data = {
        'motorcycles': motorcycle_schema.dump(motorcycles)
    }
    return Response.success(MOTORCYCLES_FETCHED, response_data, 200)
