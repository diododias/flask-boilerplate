from src.application_business.interfaces.invalid_token_repository import IInvalidTokenRepository
from src.application_business.interfaces.invalidate_token_usecase import IInvalidateTokenUseCase


class InvalidateTokenUseCase(IInvalidateTokenUseCase):

    def __init__(self, repository: IInvalidTokenRepository):
        self.repository = repository

    def execute(self, auth_token: str):
        """
        Save a token, later use of that token, authorization will be denied
        :param auth_token:
        :return:
        """
        return self.repository.invalidate_token(auth_token)
