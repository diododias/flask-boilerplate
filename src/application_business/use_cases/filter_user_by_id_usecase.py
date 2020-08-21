from sqlalchemy.dialects.postgresql import UUID
from src.application_business.interfaces.user_repository import IUserRepository
from src.application_business.interfaces.filter_user_by_id_usecase import IFilterUserByIdUseCase


class FilterUserByIdUseCase(IFilterUserByIdUseCase):

    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def execute(self, id: UUID(as_uuid=True)):
        return self.repository.filter_by_id(value=id)
