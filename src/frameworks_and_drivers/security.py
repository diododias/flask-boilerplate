from flask import abort
from functools import wraps
from flask_bcrypt import Bcrypt
from src.application_business.services.responses_service import Responses
from src.frameworks_and_drivers.factories.token_service import create_token_service


bcrypt = Bcrypt()


class Security:
    _token_service = create_token_service()

    @classmethod
    def login_required(cls, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = cls._token_service.decode_auth_token()
            if resp.get('user_id', None):
                return f(*args, **kwargs)
            abort(Responses.unauthorized())

        return decorated_function
