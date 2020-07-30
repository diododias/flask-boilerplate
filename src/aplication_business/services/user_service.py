from src.resources.database.helpers import validate_uuid
from src.aplication_business.services.token_service import TokenService
from src.aplication_business.services.responses_service import Responses
from src.resources.database.repository.user_repository import UserRepository
from src.aplication_business.services.password_service import PasswordService
from src.aplication_business.use_cases.user_usecases import UserUseCase


class UserService:
    """
    Services about all user interation
    """
    def __init__(self, repository: UserRepository, token_service: TokenService, password_service: PasswordService):
        self._password_service = password_service
        self._token_service = token_service
        self._user_usecase = UserUseCase(repository=repository)

    @staticmethod
    def _value_is_none_or_empty(value) -> bool:
        if value is None or len(value) == 0:
            return True
        else:
            return False

    def _validate_fields(self, post_data: dict) -> Responses.response_base:
        if self._value_is_none_or_empty(post_data.get('email')):
            return Responses.invalid_entity(f'Invalid value to email field.')
        if self._value_is_none_or_empty(post_data.get('password')):
            return Responses.invalid_entity(f'Invalid value to password field.')

        if post_data.get('roles', None) is not None:
            del post_data['roles']

        if post_data.get('is_superuser', None) is not None:
            del post_data['is_superuser']

    def register_user(self, post_data: dict) -> Responses.response_base:
        self._validate_fields(post_data)
        user = self._user_usecase.find_user_by_email(post_data.get('email'))
        if not user:
            try:
                user = self._user_usecase.create_user(post_data)
                response_object = {
                    'auth_token': TokenService.encode_auth_token(user.id)
                }
                return Responses.ok(response_object)
            except Exception as e:
                return Responses.bad_request(str(e))
        else:
            return Responses.accepted(message="User already exists.")

    def login_user(self, post_data: dict) -> Responses.response_base():
        try:
            self._validate_fields(post_data)
            user = self._user_usecase.find_user_by_email(post_data.get('email'))
            if user:
                if self._password_service.check_password(user.password, post_data.get('password')):
                    auth_token = TokenService.encode_auth_token(user.id)
                    if auth_token:
                        response_object = {
                            'auth_token': auth_token
                        }
                        return Responses.ok(data=response_object)
                    else:
                        return Responses.bad_request(message="JWT Token not generated")
                else:
                    return Responses.bad_request(message="Bad password.")
            else:
                return Responses.not_found('User not found.')
        except Exception as e:
            return Responses.bad_request(message=str(e))

    def logout_user(self, auth_token) -> Responses.response_base():
        if auth_token:
            resp = self._token_service.decode_auth_token(auth_token)
            if validate_uuid(resp):
                self._token_service.include_token_blacklist(auth_token)
                return Responses.ok(message='Successfully logged out.')
            else:
                return Responses.bad_request(message=resp)
        else:
            return Responses.bad_request(message='Provide a valid authorization header.')

    def status_user(self, auth_token) -> Responses.response_base():
        if auth_token:
            resp = self._token_service.decode_auth_token(auth_token)
            if validate_uuid(resp):
                user = self._user_usecase.find_user_by_id(resp)
                response_object = {
                        'user_id': str(user.id),
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'roles': user.roles,
                        'is_superuser': user.is_superuser,
                        'created': str(user.created_at)
                    }
                return Responses.ok(data=response_object)
            return Responses.unauthorized(message=resp)
        else:
            return Responses.bad_request(message='Provide a valid auth token.')
