from mock import patch
from src.resources.database.repository.role_repository import RoleRepository


@patch('src.resources.database.db.session')
def test_role_repository_filter_by_name(db_mock):
    repo = RoleRepository(db_mock)
    role = repo.filter_by_name("default")
    assert role is not None
    db_mock.query.assert_called()


@patch('src.resources.database.db.session')
def test_role_repository_filter_by_id(db_mock):
    repo = RoleRepository(db_mock)
    role = repo.filter_by_id("fiction-id")
    assert role is not None
    db_mock.query.assert_called()
