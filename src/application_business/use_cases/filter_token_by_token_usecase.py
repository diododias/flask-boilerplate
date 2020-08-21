from src.application_business.interfaces.invalid_token_repository import IInvalidTokenRepository
from src.application_business.interfaces.filter_token_by_token_usecase import IFilterTokenByTokenUseCase


class FilterTokenByTokenUseCase(IFilterTokenByTokenUseCase):

    def __init__(self, repository: IInvalidTokenRepository):
        self.repository = repository

    def execute(self, auth_token: str):
        return self.repository.filter_by_token(auth_token)
