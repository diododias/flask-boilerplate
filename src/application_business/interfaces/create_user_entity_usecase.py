from abc import ABCMeta, abstractmethod
from src.frameworks_and_drivers.database import db


class ICreateUserEntityUseCase(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute(cursor: db.Model):
        raise NotImplementedError
