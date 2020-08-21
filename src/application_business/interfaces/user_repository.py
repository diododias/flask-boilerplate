from abc import abstractmethod
from src.frameworks_and_drivers.database import db
from src.application_business.interfaces.base_repository import IBaseRepository


class IUserRepository(IBaseRepository):
    @abstractmethod
    def create_user(self, user_data: dict) -> db.Model:
        raise NotImplementedError

    @abstractmethod
    def filter_by_email(self, value: str):
        raise NotImplementedError

    @abstractmethod
    def filter_by_id(self, value: str):
        raise NotImplementedError
