import requests
from tests.utils.link import get_full_link, ApiRoutesCatfacts
from tests.utils.assertions import validate_schema, assert_status_code


def test_get_breeds_wo_params():
    breeds_url = get_full_link(ApiRoutesCatfacts.BREEDS)
    response = requests.get(url=breeds_url)
    assert_status_code(response.status_code, 200)
    for breed in response.json()['data']:
        validate_schema(breed, 'breed.json')


def test_get_breeds_with_params():
    breeds_url = get_full_link(ApiRoutesCatfacts.BREEDS)
    response = requests.get(url=breeds_url, params={'limit': 1})
    assert_status_code(response.status_code, 200)
    response_data = response.json()['data']
    for breed in response_data:
        validate_schema(breed, 'breed.json')
    assert len(response_data) == 1


def test_get_fact():
    fact_url = get_full_link(ApiRoutesCatfacts.FACT)
    response = requests.get(url=fact_url)
    assert_status_code(response.status_code, 200)
    validate_schema(response.json(), 'fact.json')

    params = {'max_length': 100}
    response_with_params = requests.get(url=fact_url, params=params)
    assert_status_code(response.status_code, 200)
    validate_schema(response.json(), 'fact.json')
    assert int(response_with_params.json()['length']) <= params.get('max_length')

