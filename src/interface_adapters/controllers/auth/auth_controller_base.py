from src.resources.security import bcrypt
from src.application_business.services.user_service import UserService
from src.application_business.services.token_service import TokenService
from src.application_business.services.password_service import PasswordService
from src.resources.database.repository.user_repository import UserRepository
from src.resources.database.repository.invalid_token_repository import InvalidTokenRepository
from src.interface_adapters.controllers.controller_base import ControllerResourceBase


class AuthControllerBase(ControllerResourceBase):
    def __init__(self, user_repository: UserRepository, token_repository: InvalidTokenRepository, bcrypt: bcrypt):
        super().__init__(token_repository=token_repository)
        self._user_service = UserService(
            repository=user_repository,
            token_service=TokenService(
                repository=token_repository
            ),
            password_service=PasswordService(bcrypt)
        )
