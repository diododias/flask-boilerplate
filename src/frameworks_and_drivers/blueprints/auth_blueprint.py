from flask import Blueprint, request
from src.frameworks_and_drivers.factories.user_service import create_user_service
from src.frameworks_and_drivers.factories.token_service import create_token_service
from src.interface_adapters.controllers.auth.login_controller import AuthLoginController
from src.interface_adapters.controllers.auth.logout_controller import AuthLogoutController
from src.interface_adapters.controllers.auth.status_controller import AuthUserStatusController
from src.interface_adapters.controllers.auth.register_controller import AuthRegisterUserController


auth_blueprint = Blueprint('auth_api', __name__)


auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=AuthRegisterUserController.as_view('auth_register',
                                                 user_service=create_user_service(),
                                                 token_service=create_token_service(),
                                                 flask_request=request),
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=AuthLoginController.as_view('auth_login',
                                          user_service=create_user_service(),
                                          token_service=create_token_service(),
                                          flask_request=request),
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/logout',
    view_func=AuthLogoutController.as_view('auth_logout',
                                           user_service=create_user_service(),
                                           token_service=create_token_service(),
                                           flask_request=request),
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/auth/status',
    view_func=AuthUserStatusController.as_view('auth_status',
                                               user_service=create_user_service(),
                                               token_service=create_token_service(),
                                               flask_request=request),
    methods=['POST']
)
