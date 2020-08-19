from sqlalchemy.dialects.postgresql import UUID
from src.frameworks_and_drivers.database import db
from src.enterprise_business.entities.user_entity import UserEntity
from src.application_business.use_cases.usecase_base import UsecaseBase


class UserUseCase(UsecaseBase):

    @staticmethod
    def _create_user_entity(cursor: db.Model):
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

    def create_user(self, post_data: dict):
        cursor = self.repository.create_user(post_data)
        return self._create_user_entity(cursor)

    def find_user_by_email(self, email: str):
        cursor = self.repository.filter_by_email(email)
        return self._create_user_entity(cursor)

    def find_user_by_id(self, id: UUID(as_uuid=True)):
        cursor = self.repository.filter_by_id(value=id)
        return self._create_user_entity(cursor)
