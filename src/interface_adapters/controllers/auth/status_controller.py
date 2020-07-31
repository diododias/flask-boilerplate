from src.interface_adapters.controllers.auth.auth_controller_base import AuthControllerBase


class AuthUserStatusController(AuthControllerBase):
    """
    Token Status
    """
    def post(self):
        user_service = self._create_user_service()
        return user_service.status_user(user_id=self.get_user_id())
