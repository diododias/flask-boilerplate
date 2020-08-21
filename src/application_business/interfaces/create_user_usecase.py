from abc import ABCMeta, abstractmethod


class ICreateUserUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, post_data: dict):
        raise NotImplementedError
