from flask import Blueprint
from src.resources.database import db
from src.resources.security import bcrypt
from src.controllers.controller_base import ControllerResourceBase
from src.aplication_business.services.user_service import UserService
from src.aplication_business.services.token_service import TokenService
from src.aplication_business.services.password_service import PasswordService
from src.resources.database.repository.user_repository import UserRepository
from src.resources.database.repository.blacklist_token_repository import BlacklistTokenRepository


auth_blueprint = Blueprint('auth_api', __name__)


class AuthControllerBase(ControllerResourceBase):
    @classmethod
    def _create_user_service(cls):
        return UserService(
            repository=UserRepository(
                database_engine=db
            ),
            token_service=TokenService(
                repository=BlacklistTokenRepository(database_engine=db)
            ),
            password_service=PasswordService(bcrypt)
        )


class AuthRegisterUser(AuthControllerBase):
    """
    User Registration Resource
    """
    def post(self):
        user_service = self._create_user_service()
        return user_service.register_user(self.get_json())


class AuthLogin(AuthControllerBase):
    """
    User Login Resource
    """
    def post(self):
        user_service = self._create_user_service()
        return user_service.login_user(self.get_json())


class AuthLogout(AuthControllerBase):
    """
    Logout Resource
    """
    def post(self):
        user_service = self._create_user_service()
        return user_service.logout_user(self.get_token())


class AuthTokenStatus(AuthControllerBase):
    """
    Token Status
    """
    def post(self):
        user_service = self._create_user_service()
        return user_service.status_user(self.get_token())


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
