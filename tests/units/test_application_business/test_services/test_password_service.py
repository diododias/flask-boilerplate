import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')

import pytest

from mock import patch
from src.application_business.services.password_service import PasswordService


@patch('src.frameworks_and_drivers.security.bcrypt')
def test_password_service_check_password(encript_mock):
    password_service = PasswordService(encrypt_engine=encript_mock)

    encript_mock.check_password_hash.return_value = True
    assert password_service.check_password("", "") is True

    encript_mock.check_password_hash.return_value = False
    assert password_service.check_password("", "") is False


def test_password_service_invalid_encript_engine():
    with pytest.raises(Exception):
        password_service = PasswordService(encrypt_engine=None)
        del password_service
