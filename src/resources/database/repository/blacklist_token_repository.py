from src.resources.database import db
from src.resources.database.repository.repository_base import RepositoryBase
from src.resources.database.models.blacklist_token import BlacklistTokenModel


class BlacklistTokenRepository(RepositoryBase):
    """
    Interface to access database user model
    """
    def __init__(self, database_engine: db):
        super().__init__(database_engine)
        self._blklist_model = BlacklistTokenModel

    def invalidate_token(self, auth_token: str):
        blacklist_token = self._blklist_model(token=auth_token)
        return self.insert_row(blacklist_token)

    def filter_by_token(self, value: str):
        return self._blklist_model.query.filter_by(token=str(value)).first()
