from mock import MagicMock
from src.application_business.use_cases.filter_token_by_token_usecase import FilterTokenByTokenUseCase


def test_filter_token_by_token():
    repo_mock = MagicMock()
    usecase = FilterTokenByTokenUseCase(repository=repo_mock)

    usecase.execute("")

    repo_mock.filter_by_token.assert_called()
