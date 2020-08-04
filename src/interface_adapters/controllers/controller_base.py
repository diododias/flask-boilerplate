from flask import request, abort
from flask.views import MethodView
from src.application_business.services.responses_service import Responses
from src.resources.flasksrc.input_validator import InputValidator


class ControllerResourceBase(MethodView):

    @classmethod
    def get_headers(cls):
        return request.headers

    @classmethod
    def get_json(cls):
        return request.get_json()

    @classmethod
    def get_json_with_schema(cls, schema):
        post_data = cls.get_json()
        if not isinstance(post_data, dict):
            abort(Responses.invalid_entity('Invalid json.'))
        return InputValidator.validate_json(schema=schema, json_data=post_data)

    @classmethod
    def validate_token(cls):
        if cls.get_headers().get('Authorization', None) is None:
            abort(Responses.invalid_entity('Missing Authorization header.'))
        return InputValidator.validate_token(cls.get_headers().get('Authorization'))

    @classmethod
    def get_token(cls):
        return cls.validate_token().get('auth_token')

    @classmethod
    def get_user_id(cls):
        return cls.validate_token().get('user_id')
