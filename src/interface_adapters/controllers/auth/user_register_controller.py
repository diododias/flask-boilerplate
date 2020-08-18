from src.interface_adapters.controllers.auth.auth_controller_base import AuthControllerBase
from src.interface_adapters.schemas.auth.register_schema import register_schema


class AuthRegisterUserController(AuthControllerBase):
    """
    User Registration Resource
    """
    def post(self):
        return self._user_service.register_user(self.get_json_with_schema(register_schema))
