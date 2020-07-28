from flask.views import MethodView
from flask import request, Blueprint
from src.drivers.database import validate_uuid
from src.drivers.security import bcrypt
from src.drivers.token import encode_auth_token, decode_auth_token
from src.drivers.database import db
from src.use_cases.request_responses import Responses
from src.drivers.database.models.user import User
from src.drivers.database.models.blacklist_token import BlacklistToken

auth_blueprint = Blueprint('auth_api', __name__)


class AuthRegisterUser(MethodView):
    """
    User Registration Resource
    """

    def post(self):
        post_data = request.get_json()
        user = User.query.filter_by(email=post_data.get('email')).first()
        if not user:
            try:
                user = User(
                    email=post_data.get('email'),
                    password=post_data.get('password'),
                    first_name=post_data.get('first_name', ''),
                    last_name=post_data.get('last_name', ''),
                    roles=[],
                    is_superuser=False
                )
                db.session.add(user)
                db.session.commit()
                auth_token = encode_auth_token(user.id)
                response_object = {
                    'auth_token': auth_token
                }
                return Responses.ok(response_object)
            except Exception as e:
                return Responses.bad_request(str(e))
        else:
            return Responses.accepted(message="User alredy exists.")


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
                    auth_token = encode_auth_token(user.id)
                    if auth_token:
                        response_object = {
                            'auth_token': auth_token
                        }
                        return Responses.ok(data=response_object)
                else:
                    return Responses.bad_request(message="Bad password.")
            else:
                return Responses.not_found('User not found.')
        except Exception as e:
            return Responses.bad_request(message=str(e))


class AuthLogout(MethodView):
    """
        Logout Resource
        """

    def post(self):
        auth_token = request.headers.get('Authorization', None)

        if auth_token:
            resp = decode_auth_token(auth_token)
            if validate_uuid(resp):
                blacklist_token = BlacklistToken(token=auth_token)
                try:
                    db.session.add(blacklist_token)
                    db.session.commit()
                    return Responses.ok(message='Successfully logged out.')
                except Exception as e:
                    return Responses.bad_request(message=str(e))
            else:
                return Responses.bad_request(message=resp)
        else:
            return Responses.bad_request(message='Provide a valid authorization header.')


class AuthTokenStatus(MethodView):
    """
    Token Status
    """
    def post(self):
        auth_token = request.headers.get('Authorization', None)
        if auth_token:
            resp = decode_auth_token(auth_token)
            if validate_uuid(resp):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                        'user_id': str(user.id),
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'roles': user.roles,
                        'is_superuser': user.is_superuser,
                        'created': str(user.created_at)
                    }
                return Responses.ok(data=response_object)
            return Responses.unauthorized(message=resp)
        else:
            return Responses.bad_request(message='Provide a valid auth token.')
        
        
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=AuthRegisterUser.as_view('auth_register'),
    methods=['POST']
)
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
auth_blueprint.add_url_rule(
    '/auth/status',
    view_func=AuthTokenStatus.as_view('auth_status'),
    methods=['POST']
)
