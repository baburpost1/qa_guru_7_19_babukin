import requests, math
from tests.utils.link import ApiRoutesRequres, get_full_link
from tests.utils.assertions import validate_schema, assert_status_code


def test_get_single_user_data():
    user_id = 2
    user_url = f"{get_full_link(ApiRoutesRequres.USER)}/{user_id}"
    response = requests.get(url=user_url)
    assert_status_code(response.status_code, 200)
    # TODO: Не нравится писать schema_name - лучше бы выбирать. Посмотреть как можно это исправить
    validate_schema(response.json(), 'get_single_user.json')
    validate_schema(response.json()['data'], 'user_data.json')
    # TODO: куча однообразных проверок, наверное можно куда-то вынести
    assert response.json()['data']['id'] == user_id
    assert response.json()['data']['email'] == 'janet.weaver@reqres.in'


def test_get_list_of_users_wo_params():
    user_list_url = get_full_link(project='requres', route=ApiRoutesRequres.USER)
    response = requests.get(user_list_url)
    assert_status_code(response.status_code, 200)
    validate_schema(response.json(), 'list_users.json')
    users = list(response.json()['data'])
    for user in users:
        validate_schema(user, 'user_data.json')


def test_get_list_of_users_with_params():
    user_list_url = get_full_link(project='requres', route=ApiRoutesRequres.USER)
    params = {'page': 1, 'per_page': 13}
    response = requests.get(url=user_list_url, params=params)
    assert_status_code(response.status_code, 200)
    validate_schema(response.json(), 'list_users.json')
    users = list(response.json()['data'])
    for user in users:
        validate_schema(user, 'user_data.json')
    assert response.json()['total_pages'] == math.ceil((response.json()['total']) / response.json()['per_page'])


def test_get_nonexistent_user():
    user_id = 99999
    user_url = f"{get_full_link(project='requres', route=ApiRoutesRequres.USER)}/{user_id}"
    response = requests.get(url=user_url)
    assert_status_code(response.status_code, 404)


def test_create_user_positive():
    create_user_url = get_full_link(project='requres', route=ApiRoutesRequres.USER)
    # TODO: а если в теле запроса  больше параметров? или какая-нибудь запустанная схема - не писать же это каждый раз руками
    body = {"name": "John Snow", "job": "knowing nothing", "test_param": "test"}
    response = requests.post(url=create_user_url, json=body)
    assert_status_code(response.status_code, 201)
    validate_schema(response.json(), 'post_users.json')
    assert response.json()['test_param'] == body.get("test_param")


def test_change_user_positive():
    user_id = 1
    update_user_link = f"{get_full_link(project='requres', route=ApiRoutesRequres.USER)}/{user_id}"
    body = {"test_param": "test"}
    response = requests.patch(url=update_user_link, json=body)
    assert_status_code(response.status_code, 200)
    validate_schema(response.json(), 'update_user.json')
    assert response.json()['test_param'] == body.get("test_param")

    response = requests.put(url=update_user_link, json=body)
    assert_status_code(response.status_code, 200)
    validate_schema(response.json(), 'update_user.json')
    assert response.json()['test_param'] == body.get("test_param")


def test_delete_user():
    user_id = 1
    delete_user_url = f"{get_full_link(project='requres', route=ApiRoutesRequres.USER)}/{user_id}"
    response = requests.delete(url=delete_user_url)
    assert_status_code(response.status_code, 204)
    assert response.text == ''
