from flask import abort
from src.application_business.services.token_service import TokenService
from src.application_business.services.responses_service import Responses
from src.frameworks_and_drivers.database.repository.user_repository import UserRepository
from src.application_business.services.password_service import PasswordService
from src.application_business.use_cases.user_usecases import UserUseCase


class UserService:
    """
    Services about all user interation
    """
    def __init__(self, repository: UserRepository, token_service: TokenService, password_service: PasswordService):
        self._password_service = password_service
        self._token_service = token_service
        self._user_usecase = UserUseCase(repository=repository)

    def register_user(self, post_data: dict) -> Responses.response_base:
        user = self._user_usecase.find_user_by_email(post_data.get('email'))
        if not user:
            try:
                user = self._user_usecase.create_user(post_data)
                response_object = {
                    'auth_token': TokenService.encode_auth_token(user.id)
                }
                return Responses.created(response_object)
            except Exception as e:
                return Responses.bad_request(str(e))
        else:
            return Responses.accepted(message="User already exists.")

    def login_user(self, post_data: dict) -> Responses.response_base():
        user = self._user_usecase.find_user_by_email(post_data.get('email'))
        if user:
            if self._password_service.check_password(user.password, post_data.get('password')):
                auth_token = TokenService.encode_auth_token(user.id)
                response_object = {
                    'auth_token': auth_token
                }
                return Responses.ok(data=response_object)
            else:
                return Responses.bad_request(message="Bad password.")
        else:
            return Responses.not_found('User not found.')

    def logout_user(self, auth_token: str) -> Responses.response_base():
        self._token_service.include_token_blacklist(auth_token)
        return Responses.ok(message='Successfully logged out.')

    def status_user(self, user_id: str) -> Responses.response_base():
        user = self._user_usecase.find_user_by_id(user_id)
        if user is None:
            abort(Responses.invalid_entity("Invalid token"))
        response_object = {
            'user_id': str(user.id),
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'roles': [role.name for role in user.roles],
            'is_superuser': user.is_superuser,
            'created': str(user.created_at)
        }
        return Responses.ok(data=response_object)
