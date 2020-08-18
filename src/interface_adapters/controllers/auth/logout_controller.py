from src.interface_adapters.controllers.auth.auth_controller_base import AuthControllerBase
from src.resources.security import Security


class AuthLogoutController(AuthControllerBase):
    """
    Logout Resource
    """
    @Security.login_required
    def post(self):
        return self._user_service.logout_user(auth_token=self.get_token())
