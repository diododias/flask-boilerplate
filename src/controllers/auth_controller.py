from flask.views import MethodView
from flask import request, Blueprint
from src.drivers.core_container import CoreContainer
from src.models.user import User
from src.use_cases.user_usecases import UserUseCase

auth_blueprint = Blueprint('auth_api', __name__)

db = CoreContainer.db
bcrypt = CoreContainer.bcrypt


class AuthRegisterUser(MethodView):
    """
    User Registration Resource
    """

    def post(self):
        post_data = request.get_json()
        user_usecase = UserUseCase(user_model=User, database_engine=CoreContainer.db)
        return user_usecase.register_user(post_data)


class AuthLogin(MethodView):
    """
    User Login Resource
    """
    def post(self):
        post_data = request.get_json()
        user_usecase = UserUseCase(user_model=User,
                                   database_engine=CoreContainer.db,
                                   encrypt_engine=CoreContainer.bcrypt)
        return user_usecase.login_user(post_data)


class AuthLogout(MethodView):
    """
        Logout Resource
        """

    def post(self):
        auth_token = request.headers.get('Authorization', None)
        user_usecase = UserUseCase(user_model=User,
                                   database_engine=CoreContainer.db,
                                   encrypt_engine=CoreContainer.bcrypt)
        return user_usecase.login_user(auth_token)


class AuthTokenStatus(MethodView):
    """
    Token Status
    """
    def post(self):
        auth_token = request.headers.get('Authorization', None)
        user_usecase = UserUseCase(user_model=User,
                                   database_engine=CoreContainer.db,
                                   encrypt_engine=CoreContainer.bcrypt)
        return user_usecase.logout_user(auth_token)
        
        
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
