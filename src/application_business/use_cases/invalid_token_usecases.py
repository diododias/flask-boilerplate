from src.frameworks_and_drivers.database import db
from src.enterprise_business.entities.token_entity import TokenEntity
from src.application_business.use_cases.usecase_base import UsecaseBase


class InvalidTokenUsecase(UsecaseBase):
    @staticmethod
    def _create_token(cursor: db.Model):
        if not isinstance(cursor, type(db.Model)):
            return cursor
        return TokenEntity(
            id=cursor.id,
            token=cursor.token,
            blacklisted_on=cursor.blacklisted_on,
            cursor=cursor
        )

    def find_token(self, auth_token: str):
        cursor = self.repository.filter_by_token(auth_token)
        return self._create_token(cursor)

    def invalidate_token(self, auth_token: str):
        return self.repository.invalidate_token(auth_token)
