from abc import ABCMeta, abstractmethod


class IFilterTokenByTokenUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, auth_token: str):
        raise NotImplementedError
