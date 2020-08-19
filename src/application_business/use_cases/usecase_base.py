from src.frameworks_and_drivers.database.repository.repository_base import RepositoryBase


class UsecaseBase:

    def __init__(self, repository: RepositoryBase):
        self.repository = repository
