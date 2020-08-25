from src.frameworks_and_drivers.database import db
from src.frameworks_and_drivers.database.repository.base_repository import RepositoryBase
from src.frameworks_and_drivers.database.models.invalid_tokens_model import InvalidToken
from src.application_business.interfaces.invalid_token_repository import IInvalidTokenRepository


class InvalidTokenRepository(RepositoryBase, IInvalidTokenRepository):
    """
    Point to access invalid_tokens table on database
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
