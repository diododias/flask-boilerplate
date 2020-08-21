import jwt
from uuid import UUID
from flask import abort
from datetime import datetime, timedelta
from src.application_business.services.responses_service import Responses
from src.application_business.interfaces.create_token_entity_usecase import ICreateTokenEntityUseCase
from src.application_business.interfaces.filter_token_by_token_usecase import IFilterTokenByTokenUseCase
from src.application_business.interfaces.invalidate_token_usecase import IInvalidateTokenUseCase
from src.application_business.interfaces.get_auth_token_usecase import IGetAuthTokenUseCase


class TokenService:

    def __init__(self, create_token_entity_usecase: ICreateTokenEntityUseCase,
                 filter_token_by_token_usecase: IFilterTokenByTokenUseCase,
                 invalidate_token_usecase: IInvalidateTokenUseCase,
                 get_auth_token: IGetAuthTokenUseCase,
                 secret: str):
        self._secret = secret
        self._filter_token = filter_token_by_token_usecase
        self._create_entity = create_token_entity_usecase
        self._invalidate_token = invalidate_token_usecase
        self._get_auth_token = get_auth_token

    def is_blacklisted(self, auth_token):
        if self._filter_token.execute(auth_token):
            return True
        else:
            return False

    def include_token_blacklist(self, auth_token):
        result = self._create_entity.execute(self._filter_token.execute(auth_token))
        if result:
            return result
        return self._invalidate_token.execute(auth_token)

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

    def decode_auth_token(self):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        auth_token = self._get_auth_token.execute()
        try:
            payload = jwt.decode(auth_token, self._secret)
            if not self.is_blacklisted(auth_token):
                uuid_obj = UUID(payload.get('sub'), version=4)
                if uuid_obj:
                    return {'user_id': payload['sub'], 'auth_token': auth_token}

            abort(Responses.invalid_entity("Invalid token"))
        except jwt.ExpiredSignatureError:
            abort(Responses.invalid_entity('Signature expired.'))
        except jwt.InvalidTokenError:
            abort(Responses.invalid_entity('Invalid token.'))
