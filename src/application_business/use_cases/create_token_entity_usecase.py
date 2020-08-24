from src.frameworks_and_drivers.database import db
from src.enterprise_business.entities.token_entity import TokenEntity
from src.application_business.interfaces.create_token_entity_usecase import ICreateTokenEntityUseCase


class CreateTokenEntityUseCase(ICreateTokenEntityUseCase):
    @staticmethod
    def execute(cursor: db.Model):
        """
        Convert token model returned from db in a invalid token entity, if cursor is not a db Model
        :param cursor: data returned by database
        :return:
        """
        if not isinstance(cursor, type(db.Model)):
            return cursor
        return TokenEntity(
            id=cursor.id,
            token=cursor.token,
            blacklisted_on=cursor.blacklisted_on,
            cursor=cursor
        )
