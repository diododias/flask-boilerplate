from src.interface_adapters.controllers.auth.auth_controller_base import AuthControllerBase
from src.interface_adapters.validator import DataValidator
from src.interface_adapters.schemas.auth.login_schema import login_schema


class AuthLoginController(AuthControllerBase):
    """
    User Login Resource
    """
    def post(self):
        user_service = self._create_user_service()
        post_data = DataValidator.validate_json(schema=login_schema, json_data=self.get_json())
        return user_service.login_user(post_data)
