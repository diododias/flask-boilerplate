import pytest

from unittest import mock
from src.interface_adapters.controllers.auth.login_controller import AuthLoginController


def return_valid_header():
    return {'Authorization': "TOKEN"}


def return_invalid_header():
    return {'Authorization': None}


def test_auth_login_controller_validate_authorization_is_none():
    with mock.patch.object(AuthLoginController, 'get_headers', new=return_invalid_header):
        controller = AuthLoginController()
        with pytest.raises(Exception):
            controller.validate_token()
