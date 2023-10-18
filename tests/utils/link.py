from enum import Enum
from tests import config


class ApiRoutesRequres(str, Enum):
    USER = '/users'
    REGISTER = '/register'
    LOGIN = '/login'
    UNKNOWN = '/unknown'


class ApiRoutesCatfacts(str, Enum):
    BREEDS = '/breeds'
    FACT = '/fact'
    FACTS = '/facts'


def get_full_link(route):
    a = type(route)
    b = route.__class__
    if str(route.__class__) == "<enum 'ApiRoutesRequres'>":
        return str(config.REQURES_BASE_PART_URL + route.value)
    if str(route.__class__) == "<enum 'ApiRoutesCatfacts'>":
        return str(config.CATFACT_BASE_PART_URL + route.value)
    else:
        return ValueError
