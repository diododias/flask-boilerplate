from src.interface_adapters.schemas.auth.login_schema import login_schema
from src.interface_adapters.controllers.auth.auth_controller_base import AuthControllerBase


class AuthLoginController(AuthControllerBase):
    """
    User Login Resource
    """
    def post(self):
        return self._user_service.login_user(self.get_json_with_schema(login_schema))
