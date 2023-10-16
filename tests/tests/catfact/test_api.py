import requests
from tests.utils.link import get_full_link, ApiRoutesCatfacts
from tests.utils.assertions import validate_schema, assert_status_code


def test_get_breeds():
    breeds_url = get_full_link(ApiRoutesCatfacts.BREEDS)
    response = requests.get(url=breeds_url)
    assert_status_code(response.status_code, 200)
    a = response.json()
    for breed in response.json()['data']:
        validate_schema(breed, 'breed.json')

