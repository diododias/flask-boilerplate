from flask.views import MethodView
from flask import request, Blueprint
from src.drivers.security import bcrypt
from src.drivers.jwt import encode_auth_token, decode_auth_token
from src.drivers.database import db
from src.use_cases.request_responses import response_base
from src.drivers.database.models.user import User
from src.drivers.database.models.token import Token

auth_blueprint = Blueprint('auth_api', __name__)


class AuthLogin(MethodView):
    """
    User Login Resource
    """
    def post(self):
        post_data = request.get_json()
        try:
            user = User.query.filter_by(email=post_data.get('email')).first()
            if user:
                if bcrypt.check_password_hash(
                    user.password, post_data.get('password')
                ):
                    auth_token = encode_auth_token(user.email)
                    print(auth_token)
                    if auth_token:
                        response_object = {
                            'status': 'success',
                            'message': 'Successfully logged in.',
                            'auth_token': auth_token
                        }
                        return response_base(response_object, 200)
                else:
                    response_object = {
                        'status': 'fail',
                        'message': 'Bad password.'
                    }
                    return response_base(response_object, 500)
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return response_base(response_object, 404)
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_base(response_object, 500)


class AuthLogout(MethodView):
    """
        Logout Resource
        """

    def post(self):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''

        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                blacklist_token = Token(token=auth_token)
                try:
                    db.session.add(blacklist_token)
                    db.session.commit()
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged out.'
                    }
                    return response_base(response_object, 200)
                except Exception as e:
                    response_object = {
                        'status': 'fail',
                        'message': e
                    }
                    return response_base(response_object, 200)
            else:
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
            return response_base(response_object, 403)


auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=AuthLogin.as_view('auth_login'),
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/auth/logout',
    view_func=AuthLogout.as_view('auth_logout'),
    methods=['POST']
)
