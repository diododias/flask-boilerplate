from flask import Blueprint
from src.interface_adapters.controllers.auth.user_register_controller import AuthRegisterUserController
from src.interface_adapters.controllers.auth.login_controller import AuthLoginController
from src.interface_adapters.controllers.auth.logout_controller import AuthLogoutController
from src.interface_adapters.controllers.auth.status_controller import AuthUserStatusController


auth_blueprint = Blueprint('auth_api', __name__)

auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=AuthRegisterUserController.as_view('auth_register'),
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=AuthLoginController.as_view('auth_login'),
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/auth/logout',
    view_func=AuthLogoutController.as_view('auth_logout'),
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/auth/status',
    view_func=AuthUserStatusController.as_view('auth_status'),
    methods=['POST']
)
