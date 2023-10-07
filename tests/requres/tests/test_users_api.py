import requests, math
from tests.requres import schemas
from tests.requres.utils.link import ApiRoutes, get_full_link
from tests.requres.utils.assertions import validate_schema, assert_status_code, load_schema


def test_get_single_user_data():
    user_id = 2
    user_url = f'{get_full_link(ApiRoutes.USER)}/{user_id}'
    response = requests.get(url=user_url)
    assert_status_code(response.status_code, 200)
    # TODO: Не нравится писать schema_name - лучше бы выбирать. Посмотреть как можно это исправить
    validate_schema(response.json(), 'get_single_user.json')
    validate_schema(response.json()['data'], 'user_data.json')
    # TODO: куча однообразных проверок, наверное можно куда-то вынести
    assert response.json()['data']['id'] == user_id
    assert response.json()['data']['email'] == 'janet.weaver@reqres.in'


def test_get_list_of_users_wo_params():
    user_list_url = get_full_link(ApiRoutes.USER)
    response = requests.get(user_list_url)
    assert_status_code(response.status_code, 200)
    validate_schema(response.json(), 'list_users.json')
    users = list(response.json()['data'])
    for user in users:
        validate_schema(user, 'user_data.json')


def test_get_list_of_users_with_params():
    user_list_url = get_full_link(ApiRoutes.USER)
    params = {'page': 1, 'per_page': 13}
    response = requests.get(url=user_list_url, params=params)
    assert_status_code(response.status_code, 200)
    validate_schema(response.json(), 'list_users.json')
    users = list(response.json()['data'])
    for user in users:
        validate_schema(user, 'user_data.json')
    assert response.json()['total_pages'] == math.ceil((response.json()['total'])/response.json()['per_page'])


def test_get_nonexistent_user():
    user_id = 2
    user_url = f'{get_full_link(ApiRoutes.USER)}/{user_id}'
