from abc import ABCMeta, abstractmethod
from sqlalchemy.dialects.postgresql import UUID


class IFilterUserByIdUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, id: UUID(as_uuid=True)):
        raise NotImplementedError
