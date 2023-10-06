import requests
from tests.requres import schemas
from tests.requres.utils.link import ApiRoutes, get_full_link
from tests.requres.utils.assertions import validate_schema, assert_status_code


def test_get_single_user_data():
    user_id=1
    user_url = f'{get_full_link(ApiRoutes.USER)}/{user_id}'
    response = requests.get(url=user_url)
    assert_status_code(response.status_code, 200)
    #TODO: Не нравится писать schema_name - лучше бы выбирать. Посмотреть как можно это исправить
    validate_schema(response.json(), 'get_single_user.json')
    # TODO: куча однообразных проверок, наверное можно куда-то вынести
    assert response.json()['data']['id'] == user_id
    assert response.json()['data']['name'] == 'janet.weaver@reqres.in'


def test_get_list_of_users_wo_params():
    user_list_url = f'{get_full_link(ApiRoutes.USER)}'
    response = requests.get(user_list_url)
    a=list(response.json()['data'])[0]
    # validate_schema(a, 'get_single_user.json'['data'])