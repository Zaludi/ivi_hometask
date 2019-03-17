import pytest


@pytest.fixture(scope="module")
def generate_correct_data():
    test_key = 'AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ',
    test_location = '55.1568242,61.3809425',
    test_radius = 100,
    test_type = 'bar'
    data = {'location': test_location, 'radius': test_radius, 'type': test_type, 'key': test_key}
    return data


@pytest.fixture(scope="module")
def generate_nonexisting_key_data():
    test_key = 'AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuW'
    test_location = '55.1568242,61.3809425'
    test_radius = 100
    test_type = 'bar'
    data = {'location': test_location, 'radius': test_radius, 'type': test_type, 'key': test_key}
    return data
