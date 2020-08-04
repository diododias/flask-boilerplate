import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')

from mock import patch
from src.application_business.services.token_service import TokenService


@patch('src.resources.database.repository.invalid_token_repository.InvalidTokenRepository')
def test_invalid_token_service_is_blacklisted(repo_mock):
    token_service = TokenService(repository=repo_mock)

    repo_mock.filter_by_token.return_value = True
    assert token_service.is_blacklisted("TOKEN") is True

    repo_mock.filter_by_token.return_value = None
    assert token_service.is_blacklisted("TOKEN") is False


@patch('src.resources.database.repository.invalid_token_repository.InvalidTokenRepository')
def test_invalid_token_service_include_token_blacklist(repo_mock):
    token_service = TokenService(repository=repo_mock)

    repo_mock.filter_by_token.return_value = True
    assert token_service.include_token_blacklist("TOKEN") is True

    repo_mock.filter_by_token.return_value = None
    repo_mock.invalidate_token.return_value = True
    assert token_service.include_token_blacklist("TOKEN") is True
    repo_mock.invalidate_token.assert_called()
