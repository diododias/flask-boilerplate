from flask import Blueprint
from src.resources.security import bcrypt
from src.resources.database import db
from src.interface_adapters.controllers.auth.user_register_controller import AuthRegisterUserController
from src.interface_adapters.controllers.auth.login_controller import AuthLoginController
from src.interface_adapters.controllers.auth.logout_controller import AuthLogoutController
from src.interface_adapters.controllers.auth.status_controller import AuthUserStatusController
from src.resources.database.repository.user_repository import UserRepository
from src.resources.database.repository.invalid_token_repository import InvalidTokenRepository


auth_blueprint = Blueprint('auth_api', __name__)


# register controllers, as_view start the controller
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=AuthRegisterUserController.as_view('auth_register',
                                                 user_repository=UserRepository(db_session=db.session),
                                                 token_repository=InvalidTokenRepository(db_session=db.session),
                                                 bcrypt=bcrypt),
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=AuthLoginController.as_view('auth_login',
                                          user_repository=UserRepository(db_session=db.session),
                                          token_repository=InvalidTokenRepository(db_session=db.session),
                                          bcrypt=bcrypt),
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/logout',
    view_func=AuthLogoutController.as_view('auth_logout',
                                           user_repository=UserRepository(db_session=db.session),
                                           token_repository=InvalidTokenRepository(db_session=db.session),
                                           bcrypt=bcrypt),
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/auth/status',
    view_func=AuthUserStatusController.as_view('auth_status',
                                               user_repository=UserRepository(db_session=db.session),
                                               token_repository=InvalidTokenRepository(db_session=db.session),
                                               bcrypt=bcrypt),
    methods=['POST']
)
