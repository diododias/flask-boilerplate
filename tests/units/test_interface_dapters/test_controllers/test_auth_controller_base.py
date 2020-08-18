import pytest
import mock

from unittest import mock
from src.interface_adapters.controllers.auth.login_controller import AuthLoginController


def return_valid_header():
    return {'Authorization': "TOKEN"}


def return_invalid_header():
    return {'Authorization': None}


@mock.patch('src.resources.flasksrc.input_validator.InputValidator')
def test_auth_login_controller_validate_authorization_is_none(input_mock):
    pass
