import jwt
import datetime

from functools import wraps
from flask import request
from src.drivers.settings import APP_ENV, settings_container
from src.drivers.database.models.blacklist_token import BlacklistToken
from src.drivers.database.models.user import User
from src.use_cases.request_responses import response_base


def encode_auth_token(user_id):
    """
    Generates the Auth Token
    param: user_email
    :return: string
    """
    try:
        payload = {
            'sub': str(user_id),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow()
        }

        return jwt.encode(
            payload=payload,
            key=settings_container.get(APP_ENV).SECRET_KEY,
            algorithm='HS256'
        ).decode()
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    Validates the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, settings_container.get(APP_ENV).SECRET_KEY)
        is_blacklisted = BlacklistToken.check_blacklisted(auth_token)
        if is_blacklisted:
            return 'Token blacklisted. Please log in again.'
        else:
            return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def login_required(return_user_id=False):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                auth_header = request.headers.get('Authorization')
                if auth_header:
                    auth_token = auth_header.split(" ")[1]
                else:
                    auth_token = ''
            except Exception as e:
                response_object = {
                    'status': 'fail',
                    'message': 'Invalid auth token header format.'
                }
                return response_base(response_object, 401)

            if auth_token:
                resp = decode_auth_token(auth_token)
                if User.check_user_is_registered(resp):
                    if return_user_id:
                        return f(*args, **kwargs, user_id=resp)
                    return f(*args, **kwargs)
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_base(response_object, 401)
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Provide a valid auth token.'
                }
                return response_base(response_object, 401)
        return decorated_function
    return decorator
