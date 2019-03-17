import pytest
from methods.nearby_search import nearby_search
from helpers.expected_results import ApiKeyResponse


@pytest.mark.positive
def test_correct_request(generate_correct_data):
    test_data = generate_correct_data
    r = nearby_search(test_data)
    assert r['status'] == 'OK'
    assert r['results'][0]['name'] == 'Craft House'


def test_nonexisting_key(generate_nonexisting_key_data):
    test_data = generate_nonexisting_key_data
    r = nearby_search(test_data)
    assert r == ApiKeyResponse.wrong_key


def test_empty_key():
    test_key = ''
    test_location = '55.1568242,61.3809425'
    test_radius = 100
    test_type = 'bar'
    r = nearby_search(test_location=test_location, test_radius=test_radius, test_type=test_type, test_key=test_key)
    assert r == ApiKeyResponse.missing_key


def test_no_key():
    test_location = '55.1568242,61.3809425'
    test_radius = 100
    test_type = 'bar'
    r = nearby_search(test_location=test_location, test_radius=test_radius, test_type=test_type)
    assert r == ApiKeyResponse.missing_key
