from mock import MagicMock
from src.application_business.use_cases.invalidate_token_usecase import InvalidateTokenUseCase


def test_invalidate_token_usecase():
    repo_mock = MagicMock()
    usecase = InvalidateTokenUseCase(repository=repo_mock)

    usecase.execute("")

    repo_mock.invalidate_token.assert_called()
