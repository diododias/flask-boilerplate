from mock import patch
from src.frameworks_and_drivers.database.repository.invalid_token_repository import InvalidTokenRepository


@patch('src.frameworks_and_drivers.database.db.session')
def test_user_repository_filter_by_token(db_mock):
    repo = InvalidTokenRepository(db_mock)
    token = repo.filter_by_token("TOKEN")
    assert token is not None
    db_mock.query.assert_called()


@patch('src.frameworks_and_drivers.database.db.session')
def test_user_repository_invalidate_token(db_mock):
    repo = InvalidTokenRepository(db_mock)
    token = repo.invalidate_token("TOKEN")
    assert token is not None
    db_mock.add.assert_called()
    db_mock.commit.assert_called()
    db_mock.refresh.assert_called()
