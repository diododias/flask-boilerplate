import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')

import pytest
from mock import patch
from src.application_business.services.user_service import UserService


@patch('src.resources.database.repository.user_repository.UserRepository')
@patch('src.application_business.services.password_service.PasswordService')
@patch('src.application_business.services.token_service.TokenService')
def test_register_user(repo_mock, pass_svc_mock, token_svc_mock):
    service = UserService(repository=repo_mock, password_service=pass_svc_mock, token_service=token_svc_mock)
    post_data = {
        'email': 'test@test.com',
        'password': '123456',
        'first_name': '',
        'last_name': ''
    }

    response = service.register_user(post_data)
    assert response is not None
    assert response.status_code == 202
    repo_mock.filter_by_email.assert_called()

    repo_mock.filter_by_email.return_value = None
    response = service.register_user(post_data)
    assert response is not None
    assert response.status_code == 201

    repo_mock.create_user.return_value = Exception()
    response = service.register_user(post_data)
    assert response is not None
    assert response.status_code == 400


@patch('src.resources.database.repository.user_repository.UserRepository')
@patch('src.application_business.services.password_service.PasswordService')
@patch('src.application_business.services.token_service.TokenService')
def test_login_user(repo_mock, pass_svc_mock, token_svc_mock):
    service = UserService(repository=repo_mock, password_service=pass_svc_mock, token_service=token_svc_mock)
    post_data = {
        'email': 'test@test.com',
        'password': '123456'
    }

    response = service.login_user(post_data)
    assert response is not None
    assert response.status_code == 200
    repo_mock.filter_by_email.assert_called()

    pass_svc_mock.check_password.return_value = False
    response = service.login_user(post_data)
    assert response is not None
    assert response.status_code == 400

    repo_mock.filter_by_email.return_value = None
    response = service.login_user(post_data)
    assert response is not None
    assert response.status_code == 404


@patch('src.resources.database.repository.user_repository.UserRepository')
@patch('src.application_business.services.password_service.PasswordService')
@patch('src.application_business.services.token_service.TokenService')
def test_logout_user(repo_mock, pass_svc_mock, token_svc_mock):
    service = UserService(repository=repo_mock, password_service=pass_svc_mock, token_service=token_svc_mock)
    response = service.logout_user("TOKEN")
    assert response is not None


@patch('src.resources.database.repository.user_repository.UserRepository')
@patch('src.application_business.services.password_service.PasswordService')
@patch('src.application_business.services.token_service.TokenService')
def test_status_user(repo_mock, pass_svc_mock, token_svc_mock):
    service = UserService(repository=repo_mock, password_service=pass_svc_mock, token_service=token_svc_mock)

    class ReturnData:
        id = ""
        email = "test@test.com"
        password = "test@test.com"
        first_name = ""
        last_name = ""
        roles = list()
        is_superuser = False
        created_at = ""

    repo_mock.filter_by_id.return_value = ReturnData
    response = service.status_user("TOKEN")
    assert response is not None
    assert response.status_code == 200

    repo_mock.filter_by_id.return_value = None
    with pytest.raises(Exception):
        service.status_user("TOKEN")
