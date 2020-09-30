""" Module for stations endpoints """

from flask import request

from config.server import application
from ..models.station import Station
from ..schemas.station import StationSchema
from ..utils.helpers.response import Response
from ..utils.helpers.messages import (KEY_REQUIRED,
                                      STATION_CREATED,
                                      STATIONS_FETCHED)
from ..utils.helpers import request_data_strip


@application.route('/stations', methods=['POST'])
def create_station():
    """ Endpoint to create the station """

    request_data = request.get_json()
    if not request_data.get('location') or not request_data.get('location').strip():
        return Response.error(KEY_REQUIRED.format('location'), 400)

    if not request_data.get('number_of_batteries'):
        return Response.error(KEY_REQUIRED.format('number_of_batteries'), 400)

    new_station = Station(**request_data_strip(request_data))
    new_station.save()
    station_schema = StationSchema()
    response_data = {
        'station': station_schema.dump(new_station)
    }
    return Response.success(STATION_CREATED, response_data, 201)


@application.route('/stations', methods=['GET'])
def get_stations():
    """ Endpoint to get the stations """

    stations = Station.query.all()

    station_schema = StationSchema(many=True)
    response_data = {
        'stations': station_schema.dump(stations)
    }
    return Response.success(STATIONS_FETCHED, response_data, 200)
