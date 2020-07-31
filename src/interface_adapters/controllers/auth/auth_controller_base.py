from src.resources.database import db
from src.resources.security import bcrypt
from src.aplication_business.services.user_service import UserService
from src.aplication_business.services.token_service import TokenService
from src.aplication_business.services.password_service import PasswordService
from src.resources.database.repository.user_repository import UserRepository
from src.resources.database.repository.blacklist_token_repository import BlacklistTokenRepository
from src.interface_adapters.controllers.controller_base import ControllerResourceBase


class AuthControllerBase(ControllerResourceBase):
    @classmethod
    def _create_user_service(cls):
        return UserService(
            repository=UserRepository(
                database_engine=db
            ),
            token_service=TokenService(
                repository=BlacklistTokenRepository(database_engine=db)
            ),
            password_service=PasswordService(bcrypt)
        )
