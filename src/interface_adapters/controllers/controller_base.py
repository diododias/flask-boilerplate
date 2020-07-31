from flask import request
from flask.views import MethodView


class ControllerResourceBase(MethodView):
    @classmethod
    def get_json(cls):
        return request.get_json()

    @classmethod
    def get_token(cls):
        return request.headers.get('Authorization', None)
