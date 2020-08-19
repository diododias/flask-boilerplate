from flask import abort, request
from functools import wraps
from flask_bcrypt import Bcrypt
from src.frameworks_and_drivers.database import db
from src.application_business.services.token_service import TokenService
from src.application_business.services.responses_service import Responses
from src.frameworks_and_drivers.database.repository.invalid_token_repository import InvalidTokenRepository
from src.frameworks_and_drivers.settings import settings_container, APP_ENV


bcrypt = Bcrypt()


class Security:
    _token_service = TokenService(repository=InvalidTokenRepository(db_session=db.session),
                                  secret=settings_container.get(APP_ENV).SECRET_KEY,
                                  request=request)

    @classmethod
    def login_required(cls, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = cls._token_service.decode_auth_token()
            if resp.get('user_id', None):
                return f(*args, **kwargs)
            abort(Responses.unauthorized())

        return decorated_function
