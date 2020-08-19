from abc import ABCMeta, abstractmethod
from src.frameworks_and_drivers.database import db


class BaseRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def _insert_row(self, entity: db.Model) -> db.Model:
        raise NotImplementedError
