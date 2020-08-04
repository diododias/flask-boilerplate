from src.resources.database import db
from src.resources.database.repository.repository_base import RepositoryBase
from src.resources.database.models.invalid_tokens_model import InvalidToken


class InvalidTokenRepository(RepositoryBase):
    """
    Interface to access database user model
    """
    def __init__(self, db_session: db.session):
        super().__init__(db_session)
        self._invalid_token_model = InvalidToken

    def invalidate_token(self, auth_token: str):
        blacklist_token = self._invalid_token_model(token=auth_token)
        return self._insert_row(blacklist_token)

    def filter_by_token(self, value: str):
        return self._db_session.query(self._invalid_token_model)\
            .filter(self._invalid_token_model.token == value).first()
