from src.resources.database import db
from src.resources.database.models.user import UserModel
from src.resources.database.repository.repository_base import RepositoryBase


class UserRepository(RepositoryBase):
    """
    Interface to access database user model
    """
    def __init__(self, database_engine: db):
        super().__init__(database_engine)
        self._user_model = UserModel

    def create_user(self, post_data: dict):
        user = self._user_model(
            email=post_data.get('email'),
            password=post_data.get('password'),
            first_name=post_data.get('first_name', ''),
            last_name=post_data.get('last_name', ''),
            roles=post_data.get('roles', []),
            is_superuser=post_data.get('is_superuser', False)
        )
        return self.insert_row(user)

    def filter_by_email(self, value: str):
        return self._user_model.query.filter_by(email=value).first()

    def filter_by_id(self, value: str):
        return self._user_model.query.filter_by(id=value).first()
