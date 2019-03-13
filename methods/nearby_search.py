import requests

nearby_search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

unused_param = 'this parameter is not used'  # TODO: исправить костыльное добавление признака неиспользуемого параметра


def nearby_search(test_key=unused_param, test_location=unused_param, test_radius=unused_param, test_type=unused_param,
                  test_rankby=unused_param, test_keyword=unused_param, test_language=unused_param):
    data = {'location': test_location, 'radius': test_radius, 'type': test_type, 'rankby': test_rankby,
            'keyword': test_keyword, 'language': test_language, 'key': test_key}
    params = {}
    for p, v in data.items():  # из указанных в тесте параметров создаем словарь с параметрами, чтобы передать в запрос
        if v != unused_param:
            params.update({p: v})
    r = requests.get(url=nearby_search_url, params=params)
    return r


