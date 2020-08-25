import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')

import pytest
from mock import MagicMock
from src.application_business.services.user_service import UserService
from src.application_business.interfaces.filter_user_by_id_usecase import IFilterUserByIdUseCase
from src.application_business.interfaces.filter_user_by_email_usecase import IFilterUserByEmailUseCase
from src.application_business.interfaces.create_user_entity_usecase import ICreateUserEntityUseCase
from src.application_business.interfaces.create_user_usecase import ICreateUserUseCase
from src.application_business.services.password_service import PasswordService
from src.application_business.services.token_service import TokenService


def test_register_user():
    pass_svc_mock = MagicMock(spec=PasswordService)
    token_svc_mock = MagicMock(spec=TokenService)
    create_entity_mock = MagicMock(spec=ICreateUserEntityUseCase)
    filter_by_email_mock = MagicMock(spec=IFilterUserByEmailUseCase)
    service = UserService(password_service=pass_svc_mock,
                          token_service=token_svc_mock,
                          filter_user_by_id_usecase=MagicMock(spec=IFilterUserByIdUseCase),
                          filter_user_by_email_usecase=filter_by_email_mock,
                          create_user_entity_usecase=create_entity_mock,
                          create_user_usecase=MagicMock(spec=ICreateUserUseCase)
                          )
    post_data = {
        'email': 'test@test.com',
        'password': '123456',
        'first_name': '',
        'last_name': ''
    }

    filter_by_email_mock.execute.return_value = True
    response = service.register_user(post_data)
    assert response is not None
    assert response.status_code == 202
    filter_by_email_mock.execute.assert_called()

    class User:
        id = "ID"

    filter_by_email_mock.execute.return_value = None
    create_entity_mock.execute.return_value = User()
    token_svc_mock.encode_auth_token.return_value = dict()
    response = service.register_user(post_data)
    assert response is not None
    assert response.status_code == 201


def test_login_user():
    pass_svc_mock = MagicMock(spec=PasswordService)
    token_svc_mock = MagicMock(spec=TokenService)
    create_entity_mock = MagicMock(spec=ICreateUserEntityUseCase)
    filter_by_email_mock = MagicMock(spec=IFilterUserByEmailUseCase)
    service = UserService(password_service=pass_svc_mock,
                          token_service=token_svc_mock,
                          filter_user_by_id_usecase=MagicMock(spec=IFilterUserByIdUseCase),
                          filter_user_by_email_usecase=filter_by_email_mock,
                          create_user_entity_usecase=create_entity_mock,
                          create_user_usecase=MagicMock(spec=ICreateUserUseCase)
                          )
    post_data = {
        'email': 'test@test.com',
        'password': '123456'
    }

    pass_svc_mock.check_password.return_value = True
    token_svc_mock.encode_auth_token.return_value = "TOKEN"
    response = service.login_user(post_data)
    assert response is not None
    assert response.status_code == 200

    pass_svc_mock.check_password.return_value = False
    response = service.login_user(post_data)
    assert response is not None
    assert response.status_code == 400

    create_entity_mock.execute.return_value = None
    filter_by_email_mock.execute.return_value = None
    response = service.login_user(post_data)
    assert response is not None
    assert response.status_code == 404


def test_logout_user():
    service = UserService(password_service=MagicMock(spec=PasswordService),
                          token_service=MagicMock(spec=TokenService),
                          filter_user_by_id_usecase=MagicMock(spec=IFilterUserByIdUseCase),
                          filter_user_by_email_usecase=MagicMock(spec=IFilterUserByEmailUseCase),
                          create_user_entity_usecase=MagicMock(spec=IFilterUserByIdUseCase),
                          create_user_usecase=MagicMock(spec=ICreateUserUseCase)
                          )
    response = service.logout_user("TOKEN")
    assert response is not None


def test_status_user():
    mock_obj = MagicMock(spec=IFilterUserByIdUseCase)
    service = UserService(password_service=MagicMock(spec=PasswordService),
                          token_service=MagicMock(spec=TokenService),
                          filter_user_by_id_usecase=MagicMock(spec=IFilterUserByIdUseCase),
                          filter_user_by_email_usecase=MagicMock(spec=IFilterUserByEmailUseCase),
                          create_user_entity_usecase=mock_obj,
                          create_user_usecase=MagicMock(spec=ICreateUserUseCase)
                          )

    class ReturnData:
        id = ""
        email = "test@test.com"
        password = "test@test.com"
        first_name = ""
        last_name = ""
        roles = list()
        is_superuser = False
        created_at = ""

    mock_obj.execute.return_value = ReturnData

    response = service.status_user("TOKEN")
    assert response is not None
    assert response.status_code == 200

    mock_obj.execute.return_value = None
    with pytest.raises(Exception):
        service.status_user("TOKEN")
