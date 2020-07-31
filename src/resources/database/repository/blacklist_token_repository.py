from src.resources.database import db
from src.resources.database.repository.repository_base import RepositoryBase
from src.resources.database.models.invalid_tokens_model import InvalidTokens


class BlacklistTokenRepository(RepositoryBase):
    """
    Interface to access database user model
    """
    def __init__(self, database_engine: db):
        super().__init__(database_engine)
        self._invalid_tokens_model = InvalidTokens

    def invalidate_token(self, auth_token: str):
        blacklist_token = self._invalid_tokens_model(token=auth_token)
        return self.insert_row(blacklist_token)

    def filter_by_token(self, value: str):
        return self._invalid_tokens_model.query.filter_by(token=str(value)).first()
