from abc import ABCMeta, abstractmethod


class IFilterUserByEmailUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, email: str):
        raise NotImplementedError
