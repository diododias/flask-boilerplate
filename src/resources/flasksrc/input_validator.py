from uuid import UUID
from flask import abort
from marshmallow import ValidationError, Schema
from src.application_business.services.responses_service import Responses
from src.application_business.services.token_service import TokenService
from src.resources.database import db
from src.resources.database.repository.invalid_token_repository import InvalidTokenRepository


class InputValidator:
    @staticmethod
    def validate_json(schema: dict, json_data: dict):
        validator = Schema.from_dict(schema)
        try:
            result = validator().load(json_data)
            return result
        except ValidationError as err:
            abort(Responses.invalid_entity(str(err)))

    @staticmethod
    def validate_token(auth_token):
        try:
            token_service = TokenService(repository=InvalidTokenRepository(db_session=db))
            decoded = token_service.decode_auth_token(auth_token)
            uuid_obj = UUID(decoded.get('user_id'), version=4)
            if uuid_obj:
                return decoded
            else:
                abort(Responses.invalid_entity("Invalid token"))
        except ValueError:
            abort(Responses.invalid_entity("Invalid token"))
