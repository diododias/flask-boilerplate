from src.resources.database import db
from src.resources.security import bcrypt
from src.application_business.services.user_service import UserService
from src.application_business.services.token_service import TokenService
from src.application_business.services.password_service import PasswordService
from src.resources.database.repository.user_repository import UserRepository
from src.resources.database.repository.invalid_token_repository import InvalidTokenRepository
from src.interface_adapters.controllers.controller_base import ControllerResourceBase


class AuthControllerBase(ControllerResourceBase):
    @classmethod
    def _create_user_service(cls):
        return UserService(
            repository=UserRepository(
                db_session=db.session
            ),
            token_service=TokenService(
                repository=InvalidTokenRepository(db_session=db.session)
            ),
            password_service=PasswordService(bcrypt)
        )
