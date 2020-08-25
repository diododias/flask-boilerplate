from mock import MagicMock
from src.application_business.use_cases.filter_user_by_email_usecase import FilterUserByEmailUseCase


def test_filter_user_by_email():
    repo_mock = MagicMock()
    usecase = FilterUserByEmailUseCase(repository=repo_mock)

    usecase.execute("")

    repo_mock.filter_by_email.assert_called()
