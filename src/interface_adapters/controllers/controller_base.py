from flask import request, abort
from flask.views import MethodView
from src.aplication_business.services.responses_service import Responses
from src.interface_adapters.validator import DataValidator


class ControllerResourceBase(MethodView):
    @classmethod
    def get_json_with_schema(cls, schema):
        post_data = request.get_json()
        if not isinstance(post_data, dict):
            abort(Responses.invalid_entity('Invalid json.'))
        return DataValidator.validate_json(schema=schema, json_data=post_data)

    @classmethod
    def validate_token(cls):
        if request.headers.get('Authorization', None) is None:
            abort(Responses.invalid_entity('Missing Authorization header.'))
        return DataValidator.validate_token(request.headers.get('Authorization'))

    @classmethod
    def get_token(cls):
        return cls.validate_token().get('auth_token')

    @classmethod
    def get_user_id(cls):
        return cls.validate_token().get('user_id')

