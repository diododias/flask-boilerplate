import jwt
from functools import wraps
from flask import request, abort
from datetime import datetime, timedelta
from src.application_business.services.responses_service import Responses
from src.resources.settings import settings_container, APP_ENV
from src.resources.database.repository.invalid_token_repository import InvalidTokenRepository
from src.application_business.use_cases.invalid_token_usecases import InvalidTokenUsecase


class TokenService:

    def __init__(self, repository: InvalidTokenRepository):
        self._blacklist_token_usecase = InvalidTokenUsecase(repository=repository)

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

    @staticmethod
    def encode_auth_token(user_id):
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
                key=settings_container.get(APP_ENV).SECRET_KEY,
                algorithm='HS256'
            ).decode()
        except Exception as e:
            return e

    def decode_auth_token(self, auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, settings_container.get(APP_ENV).SECRET_KEY)
            if self.is_blacklisted(auth_token):
                abort(Responses.invalid_entity('Token blacklisted. Please log in again.'))
            else:
                return {'user_id': payload['sub'], 'auth_token': auth_token}
        except jwt.ExpiredSignatureError:
            abort(Responses.invalid_entity('Signature expired. Please log in again.'))
        except jwt.InvalidTokenError:
            abort(Responses.invalid_entity('Invalid token. Please log in again.'))

    def login_required(self, return_user_id=False):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                try:
                    auth_header = request.headers.get('Authorization')
                    if auth_header:
                        auth_token = auth_header.split(" ")[1]
                    else:
                        auth_token = ''
                except Exception:
                    return abort(Responses.unauthorized(message='Invalid auth token header format.'))

                if auth_token:
                    resp = self.decode_auth_token(auth_token)
                    """if Users.check_user_is_registered(resp):
                        if return_user_id:
                            return f(*args, **kwargs, user_id=resp)
                        return f(*args, **kwargs)"""
                    return abort(Responses.unauthorized(message=resp))
                else:
                    return abort(Responses.unauthorized(message='Provide a valid auth token.'))
            return decorated_function
        return decorator