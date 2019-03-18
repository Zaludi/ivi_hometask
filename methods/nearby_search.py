import requests

nearby_search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'


def nearby_search(test_data):
    params = {}  # из указанных в тесте параметров создаем словарь с параметрами, чтобы передать в запрос
    for p, v in test_data.items():
        if v is not None:
            params.update({p: v})
    r = requests.get(url=nearby_search_url, params=params)
    response = r.json()
    assert r.status_code == 200
    return response
