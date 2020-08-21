from src.frameworks_and_drivers.database import db
from src.enterprise_business.entities.user_entity import UserEntity
from src.application_business.interfaces.create_user_entity_usecase import ICreateUserEntityUseCase


class CreateUserEntityUseCase(ICreateUserEntityUseCase):

    @staticmethod
    def execute(cursor: db.Model):
        if not isinstance(cursor, type(db.Model)):
            return cursor
        return UserEntity(
            id=cursor.id,
            email=cursor.email,
            password=cursor.password,
            first_name=cursor.first_name,
            last_name=cursor.last_name,
            roles=cursor.roles,
            is_superuser=cursor.is_superuser,
            created_at=cursor.created_at,
            cursor=cursor
        )
