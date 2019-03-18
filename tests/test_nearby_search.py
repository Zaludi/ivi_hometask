import pytest
from methods.nearby_search import nearby_search
from helpers.expected_results import ApiKeyResponse


@pytest.mark.positive
def test_correct_request(generate_correct_data):
    test_data = generate_correct_data
    r = nearby_search(test_data)
    assert r['status'] == 'OK'
    assert r['results'][0]['name'] == 'Craft House'


def test_wrong_key(generate_wrong_key_data):
    test_data = generate_wrong_key_data
    r = nearby_search(test_data)
    assert r == ApiKeyResponse.wrong_key


def test_no_key(generate_no_key_data):
    test_data = generate_no_key_data
    r = nearby_search(test_data)
    assert r == ApiKeyResponse.missing_key
