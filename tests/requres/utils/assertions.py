from jsonschema import validate
import os, json


def load_schema(name):
    path = os.path.join('../schemas', name)
    with open(path) as file:
        schema = json.loads(file.read())
    return schema


# TODO: добавить шаг аллюра
def validate_schema(current_response, schema_name):
    schema = load_schema(schema_name)
    validate(instance=current_response, schema=schema)

# TODO: добавить шаг аллюра
def assert_status_code(current_status_code, expected_status_code):
    assert current_status_code == expected_status_code, f'Current status_code == {current_status_code}; Expected status_code == {expected_status_code} '

def assert_empty_response(response):
    assert response.text == '{}'