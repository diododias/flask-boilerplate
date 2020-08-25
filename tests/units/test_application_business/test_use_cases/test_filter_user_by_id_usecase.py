from mock import MagicMock
from src.application_business.use_cases.filter_user_by_id_usecase import FilterUserByIdUseCase


def test_filter_user_by_id():
    repo_mock = MagicMock()
    usecase = FilterUserByIdUseCase(repository=repo_mock)

    usecase.execute("")

    repo_mock.filter_by_id.assert_called()
