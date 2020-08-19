import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')

import pytest
import uuid
from flask import request
from mock import patch, Mock, MagicMock
from src.application_business.services.token_service import TokenService
from src.frameworks_and_drivers.database.repository.invalid_token_repository import InvalidTokenRepository

rq = MagicMock(spec=request)


@patch('src.frameworks_and_drivers.database.repository.invalid_token_repository.InvalidTokenRepository')
def test_invalid_token_service_is_blacklisted(repo_mock):
    token_service = TokenService(repository=repo_mock, secret="XXX", request=rq)

    repo_mock.filter_by_token.return_value = True
    assert token_service.is_blacklisted("TOKEN") is True

    repo_mock.filter_by_token.return_value = None
    assert token_service.is_blacklisted("TOKEN") is False


@patch('src.frameworks_and_drivers.database.repository.invalid_token_repository.InvalidTokenRepository')
def test_invalid_token_service_include_token_blacklist(repo_mock):
    token_service = TokenService(repository=repo_mock, secret="XXX", request=rq)

    repo_mock.filter_by_token.return_value = True
    assert token_service.include_token_blacklist("TOKEN") is True

    repo_mock.filter_by_token.return_value = None
    repo_mock.invalidate_token.return_value = True
    assert token_service.include_token_blacklist("TOKEN") is True
    repo_mock.invalidate_token.assert_called()


@patch('src.application_business.services.token_service.TokenService.get_auth_token')
def test_decode_auth_token_invalid_token(service_mock):
    token_service = TokenService(repository=Mock(spec=InvalidTokenRepository), secret="XXX", request=rq)
    service_mock.return_value = "INVALID TOKEN"

    with pytest.raises(Exception):
        token_service.decode_auth_token()


def test_decode_auth_token_successfull():
    repo_mock = MagicMock(spec=InvalidTokenRepository)
    token_service = TokenService(repository=repo_mock, secret="XXX", request=rq)

    repo_mock.filter_by_token.return_value = None

    rq.headers = {'Authorization': token_service.encode_auth_token(str(uuid.uuid4()))}

    decoded = token_service.decode_auth_token()

    assert decoded is not None
    assert decoded.get('user_id', None) is not None
    assert decoded.get('auth_token', None) is not None
    assert decoded.get('auth_token') == rq.headers.get('Authorization')
