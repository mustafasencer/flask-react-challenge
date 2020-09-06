import requests
import urllib

from flask import current_app
from requests import HTTPError

from api.utils.error import AppError

service_url = "https://geocode.search.hereapi.com/v1/geocode"


def _calculate_distance(coords_1, coords_2):
    import geopy.distance
    return geopy.distance.geodesic((coords_1['lat'], coords_1['lng']), (coords_2['lat'], coords_2['lng'])).km


def _fetch(address):
    q = {
        "q": address,
        "apiKey": current_app.config['HERE_API_KEY']
    }
    query_string = urllib.parse.urlencode(q)
    try:
        response = requests.get(f'{service_url}?{query_string}').json()
    except HTTPError as ex:
        raise AppError(
            status=400,
            err_code='errors.hereApiError',
            err_msg=f'{ex.response.body}'
        )
    except ConnectionError as ex:
        raise AppError(
            status=400,
            err_code='errors.hereApiError',
            err_msg=f'{ex[:1000]}'
        )
    if not response['items']:
        raise AppError(
            status=400,
            err_code='errors.provideValidAddress',
            err_msg=f'Please provide a valid address!'
        )
    return response['items'][0]['position']


def get_nearest_agency(start_address, agencies):
    start_coords = _fetch(start_address)
    distances = [{"distance": _calculate_distance(start_coords, _fetch(row_item.address)), "agency": row_item} for
                 row_item in agencies]
    return min(distances, key=lambda x: x['distance'])['agency']
