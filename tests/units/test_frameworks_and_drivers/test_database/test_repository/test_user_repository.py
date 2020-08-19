from mock import patch
from src.frameworks_and_drivers.database.repository.user_repository import UserRepository


@patch('src.frameworks_and_drivers.database.db.session')
def test_user_repository_find_by_name(db_mock):
    repo = UserRepository(db_mock)
    user = repo.filter_by_email("test@test.com")
    assert user is not None
    db_mock.query.assert_called()


@patch('src.frameworks_and_drivers.database.db.session')
def test_user_repository_find_by_id(db_mock):
    repo = UserRepository(db_mock)
    user = repo.filter_by_id("fiction-id")
    assert user is not None
    db_mock.query.assert_called()


@patch('src.frameworks_and_drivers.database.db.session')
def test_user_repository_create(db_mock):
    repo = UserRepository(db_mock)
    user_data = {
        'email': 'test@test.com',
        'password': '123456',
        'first_name': '',
        'last_name': ''
    }
    user = repo.create_user(user_data)
    assert user is not None
    db_mock.query.assert_called()
