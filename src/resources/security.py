from flask import abort
from functools import wraps
from flask_bcrypt import Bcrypt
from src.resources.database import db
from src.application_business.services.token_service import TokenService
from src.application_business.services.responses_service import Responses
from src.resources.database.repository.invalid_token_repository import InvalidTokenRepository


bcrypt = Bcrypt()


class Security:
    _token_service = TokenService(repository=InvalidTokenRepository(db_session=db.session))

    @classmethod
    def login_required(cls, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = cls._token_service.decode_auth_token()
            if resp.get('user_id', None):
                return f(*args, **kwargs)

            abort(Responses.unauthorized())

        return decorated_function
