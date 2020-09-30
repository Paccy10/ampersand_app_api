""" Module for batteries endpoints """

from flask import request

from config.server import application
from ..models.battery import Battery
from ..schemas.battery import BatterySchema
from ..utils.helpers.response import Response
from ..utils.helpers.messages import (KEY_REQUIRED,
                                      BATTERY_CREATED,
                                      BATTERY_EXISTS,
                                      BATTERIES_FETCHED)
from ..utils.helpers import request_data_strip


@application.route('/batteries', methods=['POST'])
def create_battery():
    """ Endpoint to create the battery """

    request_data = request.get_json()
    if not request_data.get('serial_number') or not request_data.get('serial_number').strip():
        return Response.error(KEY_REQUIRED.format('serial_number'), 400)

    if not request_data.get('capacity'):
        return Response.error(KEY_REQUIRED.format('capacity'), 400)

    battery = Battery.query.filter_by(
        serial_number=request_data.get('serial_number').strip()).first()
    if battery:
        return Response.error(BATTERY_EXISTS, 409)

    new_battery = Battery(**request_data_strip(request_data))
    new_battery.save()
    battery_schema = BatterySchema()
    response_data = {
        'battery': battery_schema.dump(new_battery)
    }
    return Response.success(BATTERY_CREATED, response_data, 201)


@application.route('/batteries', methods=['GET'])
def get_batteries():
    """ Endpoint to get the batteries """

    batteries = Battery.query.all()

    battery_schema = BatterySchema(many=True)
    response_data = {
        'batteries': battery_schema.dump(batteries)
    }
    return Response.success(BATTERIES_FETCHED, response_data, 200)
