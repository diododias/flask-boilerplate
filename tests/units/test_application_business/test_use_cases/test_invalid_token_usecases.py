import uuid
import mock

from mock import patch
from datetime import datetime
from src.application_business.use_cases.invalid_token_usecases import InvalidTokenUsecase
from src.resources.database import db
from src.entities.token_entity import TokenEntity


def mock_invalid_token_model():
    mock_model = mock.Mock(spec=type(db.Model))
    mock_model.id = uuid.uuid4()
    mock_model.token = "TOKEN"
    mock_model.blacklisted_on = datetime.now()
    mock_model.cursor = None
    return mock_model


@patch('src.resources.database.repository.invalid_token_repository.InvalidTokenRepository')
def test_invalid_token_usercase_find_token(mock_repo):
    invalid_token_usecase = InvalidTokenUsecase(repository=mock_repo)
    token = invalid_token_usecase.find_token("TOKEN")
    assert token is not None
    mock_repo.filter_by_token.assert_called_once()

    mock_repo.filter_by_token.return_value = mock_invalid_token_model()
    token = invalid_token_usecase.find_token("TOKEN2")
    assert token is not None
    assert isinstance(token, TokenEntity)


@patch('src.resources.database.repository.invalid_token_repository.InvalidTokenRepository')
def test_invalid_token_usercase_invalidate_token(mock_repo):
    invalid_token_usecase = InvalidTokenUsecase(repository=mock_repo)
    token = invalid_token_usecase.invalidate_token("TOKEN")
    assert token is not None
    mock_repo.invalidate_token.assert_called_once()
