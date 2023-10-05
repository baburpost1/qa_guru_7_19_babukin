import requests
from tests.requres import schemas
from tests.requres.utils import ApiRoutes, get_full_link


def test_get_single_user_data():
    url = get_full_link(ApiRoutes.USER)
    print(url)