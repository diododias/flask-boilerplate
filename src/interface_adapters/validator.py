from flask import abort
from marshmallow import ValidationError, Schema
from src.aplication_business.services.responses_service import Responses


def validate_json(schema: dict, json_data: dict):
    validator = Schema.from_dict(schema)
    try:
        result = validator().load(json_data)
        return result
    except ValidationError as err:
        abort(Responses.invalid_entity(str(err)))
