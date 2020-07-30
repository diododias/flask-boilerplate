from src.resources.database import validate_uuid
from src.resources.database.models.user import UserModel
from src.resources.database.repository.user_repository import UserRepository
from src.aplication_business.use_cases.responses_usecases import Responses
from src.aplication_business.use_cases.database_usecases import DatabaseUsecase
from src.aplication_business.use_cases.password_usecase import PasswordUseCase
from src.resources.database.models.blacklist_token import BlacklistTokenModel
from src.resources.database import db
from src.resources.security import bcrypt
from src.resources.token import JWTService


class UserUseCase:
    _user_repository: type(UserRepository)

    def __init__(self, encrypt_engine: bcrypt, repository: UserRepository):
        self._user_model = UserModel
        self._user_repository = repository
        self._password_usecase = PasswordUseCase(encrypt_engine)

    def create_user(self, post_data: dict):
        return self._user_repository.create_user(
            email=post_data.get('email'),
            password=post_data.get('password'),
            first_name=post_data.get('first_name', ''),
            last_name=post_data.get('last_name', ''),
            roles=post_data.get('roles', []),
            is_superuser=post_data.get('is_superuser', False)
        )
