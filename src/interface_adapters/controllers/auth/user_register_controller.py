from src.interface_adapters.controllers.auth.auth_controller_base import AuthControllerBase
from src.interface_adapters.validator import DataValidator
from src.interface_adapters.schemas.auth.register_schema import register_schema


class AuthRegisterUserController(AuthControllerBase):
    """
    User Registration Resource
    """
    def post(self):
        user_service = self._create_user_service()
        post_data = DataValidator.validate_json(schema=register_schema, json_data=self.get_json())
        return user_service.register_user(post_data)
