from flask import abort, request
from src.application_business.services.responses_service import Responses
from src.application_business.interfaces.get_auth_token_usecase import IGetAuthTokenUseCase


class GetAuthTokenUseCase(IGetAuthTokenUseCase):
    def __init__(self, request: request):
        self._request = request

    def execute(self):
        auth_header = self._request.headers.get('Authorization', None)
        if auth_header is not None and 'Bearer ' in auth_header:
            auth_token = auth_header[7:]
        else:
            auth_token = auth_header
        return auth_token if auth_token is not None else abort(Responses.invalid_entity("Invalid token"))
