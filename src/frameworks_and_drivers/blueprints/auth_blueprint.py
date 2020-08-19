from flask import Blueprint, request
from src.frameworks_and_drivers.security import bcrypt
from src.frameworks_and_drivers.database import db
from src.interface_adapters.controllers.auth.user_register_controller import AuthRegisterUserController
from src.interface_adapters.controllers.auth.login_controller import AuthLoginController
from src.interface_adapters.controllers.auth.logout_controller import AuthLogoutController
from src.interface_adapters.controllers.auth.status_controller import AuthUserStatusController
from src.frameworks_and_drivers.database.repository.user_repository import UserRepository
from src.frameworks_and_drivers.database.repository.invalid_token_repository import InvalidTokenRepository
from src.application_business.services.user_service import UserService
from src.application_business.services.token_service import TokenService
from src.application_business.services.password_service import PasswordService
from src.application_business.use_cases.user_usecases import UserUseCase
from src.frameworks_and_drivers.settings import settings_container, APP_ENV

auth_blueprint = Blueprint('auth_api', __name__)


token_service = TokenService(repository=InvalidTokenRepository(db_session=db.session),
                             secret=settings_container.get(APP_ENV).SECRET_KEY,
                             request=request)

password_service = PasswordService(encrypt_engine=bcrypt)

user_service = UserService(user_usecase=UserUseCase(repository=UserRepository(db_session=db.session)),
                           token_service=token_service,
                           password_service=password_service)


# register controllers, as_view start the controller injecting dependencies
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=AuthRegisterUserController.as_view('auth_register', user_service=user_service,
                                                 token_service=token_service),
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=AuthLoginController.as_view('auth_login',user_service=user_service,
                                                 token_service=token_service),
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/logout',
    view_func=AuthLogoutController.as_view('auth_logout',user_service=user_service,
                                                 token_service=token_service),
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/auth/status',
    view_func=AuthUserStatusController.as_view('auth_status',user_service=user_service,
                                                 token_service=token_service),
    methods=['POST']
)
