import uuid
import mock

from datetime import datetime
from unittest.mock import patch
from src.resources.database import db
from src.entities.user_entity import UserEntity
from src.application_business.use_cases.user_usecases import UserUseCase


def mock_user_entity():
    return UserEntity(
        id=uuid.uuid4(),
        email="",
        password="",
        first_name="",
        last_name="",
        roles=list(),
        is_superuser=False,
        created_at=datetime.now(),
        cursor=None
    )


def mock_user_model():
    mock_model = mock.Mock(spec=type(db.Model))
    mock_model.id = uuid.uuid4()
    mock_model.email = "test@test.com"
    mock_model.password = "123456"
    mock_model.first_name = ""
    mock_model.last_name = ""
    mock_model.roles = list()
    mock_model.is_superuser = False
    mock_model.created_at = datetime.now()
    mock_model.cursor = None
    return mock_model


@patch('src.resources.database.repository.user_repository.UserRepository')
def test_user_usecase_creation(mock_repo):
    mock_repo.create_user.return_value = mock_user_entity()
    post_data = {
        'email': "",
        'password': ""
    }
    user_use_case = UserUseCase(repository=mock_repo)
    user = user_use_case.create_user(post_data)
    assert user is not None
    assert isinstance(user, UserEntity)
    assert user.email == ""
    assert user.password == ""


@patch('src.resources.database.repository.user_repository.UserRepository')
def test_user_usecase_find_user_by_email(mock_repo):
    mock_repo.filter_by_email.return_value = mock_user_model()
    user_use_case = UserUseCase(repository=mock_repo)
    user = user_use_case.find_user_by_email('test@test.com')
    assert user is not None
    assert isinstance(user, UserEntity)
    assert user.email == "test@test.com"
    assert user.password == "123456"
    assert mock_repo.called_with('test@test.com')


@patch('src.resources.database.repository.user_repository.UserRepository')
def test_user_usecase_find_user_by_id(mock_repo):
    mock_repo.filter_by_id.return_value = mock_user_model()
    user_use_case = UserUseCase(repository=mock_repo)
    user_id = uuid.uuid4()
    user = user_use_case.find_user_by_id(id=user_id)
    assert user is not None
    assert isinstance(user, UserEntity)
    assert user.email == "test@test.com"
    assert user.password == "123456"
    mock_repo.filter_by_id.assert_called()
    mock_repo.filter_by_id.assert_called_with(value=user_id)


@patch('src.resources.database.repository.user_repository.UserRepository')
def test_user_usecase_create_user_entity_invalid_input(mock_repo):
    mock_repo.filter_by_id.return_value = True
    user_use_case = UserUseCase(repository=mock_repo)
    user_id = uuid.uuid4()
    user = user_use_case.find_user_by_id(id=user_id)
    assert user is not None
    assert isinstance(user, bool)
