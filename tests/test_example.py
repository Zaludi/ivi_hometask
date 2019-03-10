from methods.base_methods import base_request


def test_example():
    test_location = '55.1568242,61.3809425'
    test_radius = 150
    test_type = 'bar'
    test_key = 'AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ'
    r = base_request(location=test_location, radius=test_radius, type=test_type, key=test_key)
    assert r.status_code == 200
    print(r.json())
