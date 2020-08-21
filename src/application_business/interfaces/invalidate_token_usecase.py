from abc import ABCMeta, abstractmethod


class IInvalidateTokenUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, auth_token: str):
        raise NotImplementedError
