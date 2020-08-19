import pytest

from marshmallow import fields, validate
from src.frameworks_and_drivers.flasksrc.input_validator import InputValidator


schema = {
    'email': fields.Str(validate=validate.Length(min=1), max=320, required=True),
    'password': fields.Str(validate=validate.Length(min=6, max=100), required=True)
}


def test_input_validator_valid_json():
    json_data = {
        'email': 'test@test.com',
        'password': '123456'
    }

    result = InputValidator.validate_json(schema=schema, json_data=json_data)
    assert isinstance(result, dict)


def test_input_validator_invalid_json():
    json_data = {
        'email': 'test@test.com',
        'xxxxx': '123456'
    }

    with pytest.raises(Exception):
        InputValidator.validate_json(schema=schema, json_data=json_data)
