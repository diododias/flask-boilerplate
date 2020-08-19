from src.interface_adapters.controllers.auth.auth_controller_base import AuthControllerBase
from src.frameworks_and_drivers.security import Security


class AuthUserStatusController(AuthControllerBase):
    """
    Token Status
    """
    @Security.login_required
    def post(self):
        return self._user_service.status_user(user_id=self.get_user_id())
