from flask import abort
from src.application_business.services.token_service import TokenService
from src.application_business.services.responses_service import Responses, Response
from src.application_business.services.password_service import PasswordService
from src.application_business.interfaces.filter_user_by_email_usecase import IFilterUserByEmailUseCase
from src.application_business.interfaces.filter_user_by_id_usecase import IFilterUserByIdUseCase
from src.application_business.interfaces.create_user_entity_usecase import ICreateUserEntityUseCase
from src.application_business.interfaces.create_user_usecase import ICreateUserUseCase


class UserService:
    """
    Services about all user interation
    """
    _create_user: ICreateUserUseCase
    _create_entity: ICreateUserEntityUseCase
    _filter_email: IFilterUserByEmailUseCase
    _filter_id: IFilterUserByIdUseCase

    def __init__(self, token_service: TokenService,
                 password_service: PasswordService,
                 filter_user_by_id_usecase: IFilterUserByIdUseCase,
                 filter_user_by_email_usecase: IFilterUserByEmailUseCase,
                 create_user_entity_usecase: ICreateUserEntityUseCase,
                 create_user_usecase: ICreateUserUseCase
                 ):
        self._password_service = password_service
        self._token_service = token_service
        self._filter_id = filter_user_by_id_usecase
        self._filter_email = filter_user_by_email_usecase
        self._create_entity = create_user_entity_usecase
        self._create_user = create_user_usecase

    def register_user(self, post_data: dict) -> Response:
        """
        Register user if there's not have registered
        :param post_data: a dict with post data, containing user information to registration
        :return: Response object
        """
        user = self._filter_email.execute(post_data.get('email'))
        if not user:
            user = self._create_entity.execute(self._create_user.execute(post_data))

            response_object = {
                'auth_token': self._token_service.encode_auth_token(user.id)
            }
            return Responses.created(response_object)
        else:
            return Responses.accepted(message="User already exists.")

    def login_user(self, post_data: dict) -> Response:
        """
        Authenticate user to login on system
        :param post_data: a dict with post data, containing user information to registration
        :return: Response object
        """
        user = self._create_entity.execute(self._filter_email.execute(post_data.get('email')))
        if user:
            if self._password_service.check_password(user.password, post_data.get('password')):
                auth_token = self._token_service.encode_auth_token(user.id)
                response_object = {
                    'auth_token': auth_token
                }
                return Responses.ok(data=response_object)
            else:
                return Responses.bad_request(message="Bad password.")
        else:
            return Responses.not_found('User not found.')

    def logout_user(self, auth_token: str) -> Response:
        """
        Logout User blacklisting JWT Token
        :param post_data: a dict with post data, containing user information to registration
        :return: Response object
        """
        if self._token_service.include_token_blacklist(auth_token):
            return Responses.ok(message='Successfully logged out.')
        else:
            return Responses.bad_request(message="Token not blacklisted")

    def status_user(self, user_id: str) -> Response:
        """
        Check user information, useful to validate if user is authenticated on the system
        :param user_id: User ID
        :return: Response object
        """
        user = self._create_entity.execute(self._filter_id.execute(user_id))
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
