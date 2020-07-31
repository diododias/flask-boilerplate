from src.interface_adapters.controllers.auth.auth_controller_base import AuthControllerBase
from src.interface_adapters.validator import DataValidator


class AuthLogoutController(AuthControllerBase):
    """
    Logout Resource
    """
    def post(self):
        user_service = self._create_user_service()
        auth_token = DataValidator.validate_token(self.get_token()).get('auth_token')
        return user_service.logout_user(auth_token=auth_token)
