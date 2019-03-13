import pytest
from methods.nearby_search import nearby_search
from helpers.expected_results import ApiKeyResponse


@pytest.mark.positive
def test_correct_request():
    test_key = 'AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ'
    test_location = '55.1568242,61.3809425'
    test_radius = 100
    test_type = 'bar'
    r = nearby_search(test_location=test_location, test_radius=test_radius, test_type=test_type, test_key=test_key)
    assert r.status_code == 200
    response = r.json()
    print(response)
    assert response['status'] == 'OK'
    assert response['results'][0]['name'] == 'Craft House'


def test_nonexisting_key():
    test_key = 'AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuW'
    test_location = '55.1568242,61.3809425'
    test_radius = 100
    test_type = 'bar'
    r = nearby_search(test_location=test_location, test_radius=test_radius, test_type=test_type, test_key=test_key)
    assert r.status_code == 200
    response = r.json()
    print(response)
    assert response == ApiKeyResponse.wrong_key


def test_empty_key():
    test_key = ''
    test_location = '55.1568242,61.3809425'
    test_radius = 100
    test_type = 'bar'
    r = nearby_search(test_location=test_location, test_radius=test_radius, test_type=test_type, test_key=test_key)
    assert r.status_code == 200
    response = r.json()
    print(response)
    assert response == ApiKeyResponse.missing_key


def test_no_key():
    test_location = '55.1568242,61.3809425'
    test_radius = 100
    test_type = 'bar'
    r = nearby_search(test_location=test_location, test_radius=test_radius, test_type=test_type)
    assert r.status_code == 200
    response = r.json()
    print(response)
    assert response == ApiKeyResponse.missing_key
