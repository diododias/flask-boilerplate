import pytest

from mock import MagicMock
from src.application_business.use_cases.get_auth_token_usecase import GetAuthTokenUseCase


def test_get_auth_token_authorization_ok():
    request_mock = MagicMock()
    usecase = GetAuthTokenUseCase(request=request_mock)
    request_mock.headers = dict()
    request_mock.headers['Authorization'] = "TOKEN"

    token = usecase.execute()

    assert token is not None
    assert token == "TOKEN"

    request_mock.headers['Authorization'] = "Bearer TOKEN"

    token = usecase.execute()

    assert token is not None
    assert token == "TOKEN"


def test_get_auth_token_authorization_fail():
    request_mock = MagicMock()
    usecase = GetAuthTokenUseCase(request=request_mock)
    request_mock.headers = dict()
    request_mock.headers['Authorization'] = None

    with pytest.raises(Exception):
        usecase.execute()
