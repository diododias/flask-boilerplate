from src.interface_adapters.controllers.auth.auth_controller_base import AuthControllerBase
from src.interface_adapters.validator import DataValidator


class AuthUserStatusController(AuthControllerBase):
    """
    Token Status
    """
    def post(self):
        user_service = self._create_user_service()
        user_id = DataValidator.validate_token(self.get_token()).get('user_id')
        return user_service.status_user(user_id=user_id)
