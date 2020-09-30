""" Module for swaps endpoints """

from flask import request

from config.server import application
from ..models.swap import Swap
from ..models.driver import Driver
from ..models.station import Station
from ..models.battery import Battery
from ..schemas.swap import SwapSchema
from ..utils.helpers.response import Response
from ..utils.helpers.messages import (KEY_REQUIRED,
                                      DRIVER_NOT_FOUND,
                                      STATION_NOT_FOUND,
                                      SWAP_CREATED,
                                      OLD_BATTERY_NOT_FOUND,
                                      NEW_BATTERY_NOT_FOUND)
from ..utils.helpers import request_data_strip


@application.route('/swaps', methods=['POST'])
def create_swap():
    """ Endpoint to create the swap """

    request_data = request.get_json()
    if not request_data.get('station_id'):
        return Response.error(KEY_REQUIRED.format('station_id'), 400)

    if not request_data.get('driver_id'):
        return Response.error(KEY_REQUIRED.format('driver_id'), 400)

    if not request_data.get('odometer'):
        return Response.error(KEY_REQUIRED.format('odometer'), 400)

    if not request_data.get('old_battery'):
        return Response.error(KEY_REQUIRED.format('old_battery'), 400)

    if not request_data.get('new_battery'):
        return Response.error(KEY_REQUIRED.format('new_battery'), 400)

    station = Station.query.filter_by(
        id=request_data.get('station_id')).first()

    if not station:
        return Response.error(STATION_NOT_FOUND, 404)

    driver = Driver.query.filter_by(
        id=request_data.get('driver_id')).first()

    if not driver:
        return Response.error(DRIVER_NOT_FOUND, 404)

    old_battery = Battery.query.filter_by(
        id=request_data.get('old_battery').get('id')).first()

    if not old_battery:
        return Response.error(OLD_BATTERY_NOT_FOUND, 404)

    new_battery = Battery.query.filter_by(
        id=request_data.get('new_battery').get('id')).first()

    if not new_battery:
        return Response.error(NEW_BATTERY_NOT_FOUND, 404)

    swap = Swap.query.filter_by(driver_id=request_data.get(
        'driver_id')).order_by(Swap.created_at.desc()).first()

    new_swap_data = {
        'driver_id': request_data.get('driver_id'),
        'station_id': request_data.get('station_id'),
        'old_battery': request_data.get('old_battery'),
        'new_battery': request_data.get('new_battery')
    }
    energy_used = None
    distance_covered = None
    if swap:
        energy_used = swap.new_battery['energy_level'] - \
            request_data.get('old_battery').get('energy_level')
        distance_covered = request_data.get('odometer') - swap.distance_covered
    else:
        battery = Battery.query.filter_by(
            id=request_data.get('old_battery').get('id')).first()
        energy_used = battery.energy_level - request_data.get(
            'old_battery').get('energy_level')
        distance_covered = request_data.get('odometer')

    new_swap_data['energy_used'] = energy_used
    new_swap_data['distance_covered'] = distance_covered

    new_swap = Swap(**new_swap_data)
    new_swap.save()
    swap_schema = SwapSchema()
    response_data = {
        'swap': swap_schema.dump(new_swap)
    }
    return Response.success(SWAP_CREATED, response_data, 201)
