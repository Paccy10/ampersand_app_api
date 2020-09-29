""" Module for motocycles endpoints """

from flask import request

from config.server import application
from ..models.motocycle import Motocycle
from ..schemas.motocycle import MotocycleSchema
from ..utils.helpers.response import Response
from ..utils.helpers.messages import (MOTOCYCLE_CREATED,
                                      KEY_REQUIRED,
                                      MOTOCYCLE_EXISTS)
from ..utils.helpers import request_data_strip


@application.route('/motocycles', methods=['POST'])
def create_motocycle():
    """ Endpoint to create the motocycle """

    request_data = request.get_json()
    if not request_data.get('serial_number') or not request_data.get('serial_number').strip():
        return Response.error(KEY_REQUIRED.format('serial_number'), 400)

    motocycle = Motocycle.query.filter(
        Motocycle.serial_number == request_data.get('serial_number').strip()).first()
    if motocycle:
        return Response.error(MOTOCYCLE_EXISTS, 409)

    new_motocycle = Motocycle(**request_data_strip(request_data))
    new_motocycle.save()
    motocycle_schema = MotocycleSchema()
    response_data = {
        'motocycle': motocycle_schema.dump(new_motocycle)
    }
    return Response.success(MOTOCYCLE_CREATED, response_data, 201)
