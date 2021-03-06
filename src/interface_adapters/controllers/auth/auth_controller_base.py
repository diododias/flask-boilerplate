from flask import request
from src.application_business.services.user_service import UserService
from src.application_business.services.token_service import TokenService
from src.interface_adapters.controllers.controller_base import ControllerResourceBase


class AuthControllerBase(ControllerResourceBase):
    def __init__(self, user_service: UserService, token_service: TokenService, flask_request: request):
        super().__init__(token_service=token_service, flask_request=flask_request)
        self._user_service = user_service
