import requests

base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'


def base_request(location, radius, type, key):
    params = {
        'location': location,
        'radius': radius,
        'type': type,
        'key': key
    }
    r = requests.get(url=base_url, params=params)
    return r
