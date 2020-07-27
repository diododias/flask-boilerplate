import jwt

from hashlib import sha1
from functools import wraps
from flask import request
from src.drivers.settings import APP_ENV, settings_container
from src.drivers.database.models.token import Token
from src.drivers.database import db
from src.use_cases.request_responses import response_base


def encode_auth_token(user_email):
    """
    Generates the Auth Token
    param: user_email
    :return: string
    """
    try:
        token = Token.query.filter_by(hash=str(sha1(user_email.encode('utf-8')).hexdigest())).first()
        if token:
            db.session.delete(token)
            db.session.commit()

        token = Token(user_email)
        db.session.add(token)
        db.session.commit()

        payload = {
            'hash': token.hash,
            'exp': token.exp,
            'iat': token.iat
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
        is_active = BlacklistToken.check_is_active(auth_token)
        if is_active is False:
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
                if not isinstance(resp, str):
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
