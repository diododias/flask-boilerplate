from uuid import UUID
from flask import abort
from marshmallow import ValidationError, Schema
from src.aplication_business.services.responses_service import Responses
from src.aplication_business.services.token_service import TokenService
from src.resources.database import db
from src.resources.database.repository.blacklist_token_repository import BlacklistTokenRepository


class DataValidator:
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
            token_service = TokenService(repository=BlacklistTokenRepository(database_engine=db))
            decoded = token_service.decode_auth_token(auth_token)
            uuid_obj = UUID(decoded.get('user_id'), version=4)
            if uuid_obj:
                return decoded
            else:
                abort(Responses.invalid_entity("Invalid token"))
        except ValueError:
            abort(Responses.invalid_entity("Invalid token"))
