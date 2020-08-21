from src.application_business.interfaces.user_repository import IUserRepository
from src.application_business.interfaces.create_user_usecase import ICreateUserUseCase


class CreateUserUseCase(ICreateUserUseCase):

    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def execute(self, post_data: dict):
        return self.repository.create_user(post_data)
