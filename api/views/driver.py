""" Module for drivers endpoints """

from flask import request

from config.server import application
from ..models.motorcycle import Motorcycle
from ..models.driver import Driver
from ..models.swap import Swap
from ..schemas.driver import DriverSchema
from ..schemas.swap import SwapSchema
from ..utils.helpers.response import Response
from ..utils.helpers.messages import (KEY_REQUIRED,
                                      MOTORCYCLE_NOT_EXIST,
                                      DRIVER_CREATED,
                                      DRIVERS_FETCHED,
                                      DRIVER_NOT_FOUND,
                                      SWAPS_FETCHED)
from ..utils.helpers import request_data_strip


@application.route('/drivers', methods=['POST'])
def create_driver():
    """ Endpoint to create the driver """

    request_data = request.get_json()
    if not request_data.get('name') or not request_data.get('name').strip():
        return Response.error(KEY_REQUIRED.format('name'), 400)

    if not request_data.get('license_number') or not request_data.get('license_number').strip():
        return Response.error(KEY_REQUIRED.format('license_number'), 400)

    if not request_data.get('motorcycle_id'):
        return Response.error(KEY_REQUIRED.format('motorcycle_id'), 400)

    motorcycle = Motorcycle.query.filter_by(
        id=request_data.get('motorcycle_id')).first()

    if not motorcycle:
        return Response.error(MOTORCYCLE_NOT_EXIST, 400)

    new_driver = Driver(**request_data_strip(request_data))
    new_driver.save()
    driver_schema = DriverSchema()
    response_data = {
        'driver': driver_schema.dump(new_driver)
    }
    return Response.success(DRIVER_CREATED, response_data, 201)


@application.route('/drivers', methods=['GET'])
def get_drivers():
    """ Endpoint to get the drivers """

    drivers = Driver.query.all()

    driver_schema = DriverSchema(many=True)
    response_data = {
        'drivers': driver_schema.dump(drivers)
    }
    return Response.success(DRIVERS_FETCHED, response_data, 200)


@application.route('/drivers/<driver_id>/swaps', methods=['GET'])
def get_driver_swaps(driver_id):
    """ Endpoint to get the driver swaps """

    driver = Driver.query.filter_by(id=driver_id).first()
    if not driver:
        return Response.error(DRIVER_NOT_FOUND, 400)

    swaps = Swap.query.filter_by(driver_id=driver_id).all()

    swap_schema = SwapSchema(many=True)
    response_data = {
        'swaps': swap_schema.dump(swaps)
    }
    return Response.success(SWAPS_FETCHED, response_data, 200)
