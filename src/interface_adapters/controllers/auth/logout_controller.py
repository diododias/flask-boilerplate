from src.interface_adapters.controllers.auth.auth_controller_base import AuthControllerBase


class AuthLogoutController(AuthControllerBase):
    """
    Logout Resource
    """
    def post(self):
        user_service = self._create_user_service()
        return user_service.logout_user(auth_token=self.get_token())
