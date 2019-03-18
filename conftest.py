# TODO: объединить в одну фикстуру
import pytest

test_location = '55.1568242,61.3809425'
test_radius = 100
test_type = 'bar'


@pytest.fixture(scope="module")
def generate_correct_data():
    test_key = 'AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ'
    data = {'location': test_location, 'radius': test_radius, 'type': test_type, 'key': test_key}
    return data


@pytest.fixture(scope="module", params=['', None])
def generate_no_key_data(request):
    test_key = request.param
    data = {'location': test_location, 'radius': test_radius, 'type': test_type, 'key': test_key}
    return data


@pytest.fixture(scope="module", params=['AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9Nmyuw', True, 0])
def generate_wrong_key_data(request):
    test_key = request.param
    data = {'location': test_location, 'radius': test_radius, 'type': test_type, 'key': test_key}
    return data
