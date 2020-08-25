from mock import MagicMock
from src.application_business.use_cases.create_user_usecase import CreateUserUseCase


def test_create_user_usecase():
    repo_mock = MagicMock()
    use_case = CreateUserUseCase(repository=repo_mock)

    use_case.execute(dict())

    repo_mock.create_user.assert_called()
