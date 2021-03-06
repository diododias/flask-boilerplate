from flask import abort, request
from flask.views import MethodView
from src.application_business.services.responses_service import Responses
from src.application_business.services.token_service import TokenService
from src.frameworks_and_drivers.flasksrc.input_validator import InputValidator


class ControllerResourceBase(MethodView):

    def __init__(self, token_service: TokenService, flask_request: request):
        self._token_service = token_service
        self._request = flask_request

    def get_headers(self):
        return self._request.headers

    def get_json(self):
        return self._request.get_json()

    def get_json_with_schema(self, schema):
        post_data = self.get_json()
        if not isinstance(post_data, dict):
            abort(Responses.invalid_entity('Invalid json.'))
        return InputValidator.validate_json(schema=schema, json_data=post_data)

    def get_token(self):
        return self._token_service.decode_auth_token().get('auth_token')

    def get_user_id(self):
        return self._token_service.decode_auth_token().get('user_id')
