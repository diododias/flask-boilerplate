from abc import ABCMeta, abstractmethod


class InvalidTokenRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def invalidate_token(self, auth_token: str):
        raise NotImplementedError

    @abstractmethod
    def filter_by_token(self, value: str):
        raise NotImplementedError
