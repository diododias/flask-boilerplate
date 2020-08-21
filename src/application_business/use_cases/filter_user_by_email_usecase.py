from src.application_business.interfaces.user_repository import IUserRepository
from src.application_business.interfaces.filter_user_by_email_usecase import IFilterUserByEmailUseCase


class FilterUserByEmailUseCase(IFilterUserByEmailUseCase):

    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def execute(self, email: str):
        return self.repository.filter_by_email(email)
