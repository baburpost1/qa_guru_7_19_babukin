from enum import Enum
import os
from tests.requres import config


class ApiRoutes(str, Enum):
    USER = '/users'
    REGISTER = '/register'
    LOGIN = '/login'
    UNKNOWN = '/unknown'

    def get_route(self):
        return self.value


def get_full_link(route: ApiRoutes):
    return str(config.BASE_PART_URL + route.value)
