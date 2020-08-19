import jwt
from uuid import UUID
from flask import abort, request
from datetime import datetime, timedelta
from src.application_business.services.responses_service import Responses
from src.application_business.interfaces.invalid_token_repository import InvalidTokenRepositoryInterface
from src.application_business.use_cases.invalid_token_usecases import InvalidTokenUsecase


class TokenService:

    def __init__(self, repository: InvalidTokenRepositoryInterface, secret: str, request: request):
        self._blacklist_token_usecase = InvalidTokenUsecase(repository=repository)
        self._secret = secret
        self._request = request

    def is_blacklisted(self, auth_token):
        if self._blacklist_token_usecase.find_token(auth_token):
            return True
        else:
            return False

    def include_token_blacklist(self, auth_token):
        result = self._blacklist_token_usecase.find_token(auth_token)
        if result:
            return result
        return self._blacklist_token_usecase.invalidate_token(auth_token)

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        param: user_id
        :return: string
        """
        try:
            payload = {
                'sub': str(user_id),
                'exp': datetime.utcnow() + timedelta(days=1),
                'iat': datetime.utcnow()
            }
            return jwt.encode(
                payload=payload,
                key=self._secret,
                algorithm='HS256'
            ).decode()
        except Exception as e:
            return e

    def get_auth_token(self):
        auth_header = self._request.headers.get('Authorization', None)

        if auth_header is not None and 'Bearer ' in auth_header:
            auth_token = auth_header[7:]

        else:
            auth_token = auth_header

        return auth_token if auth_token is not None else abort(Responses.invalid_entity("Invalid token"))

    def decode_auth_token(self):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        auth_token = self.get_auth_token()
        try:
            payload = jwt.decode(auth_token, self._secret)
            if self.is_blacklisted(auth_token) is False:
                uuid_obj = UUID(payload.get('sub'), version=4)
                if uuid_obj:
                    return {'user_id': payload['sub'], 'auth_token': auth_token}

            abort(Responses.invalid_entity("Invalid token"))
        except jwt.ExpiredSignatureError:
            abort(Responses.invalid_entity('Signature expired.'))
        except jwt.InvalidTokenError:
            abort(Responses.invalid_entity('Invalid token.'))
