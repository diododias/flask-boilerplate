from abc import ABCMeta, abstractmethod


class IGetAuthTokenUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        raise NotImplementedError
