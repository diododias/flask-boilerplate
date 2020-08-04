from src.resources.database import db
from src.resources.database.models.users_model import User
from src.resources.database.repository.repository_base import RepositoryBase
from src.resources.database.repository.role_repository import RoleRepository


class UserRepository(RepositoryBase):
    """
    Interface to access database user model
    """
    def __init__(self, db_session: db.session):
        super().__init__(db_session)
        self._user_model = User
        self._role_repository = RoleRepository(db_session)

    def create_user(self, user_data: dict):
        """
        Create user model and insert in DB
        when create user, default role is assigment to user
        :param user_data: data about user
        :return:
        """
        role = self._role_repository.filter_by_name("default")
        user = self._user_model(
            email=user_data.get('email'),
            password=user_data.get('password'),
            first_name=user_data.get('first_name', ''),
            last_name=user_data.get('last_name', ''),
            roles=role,
            is_superuser=user_data.get('is_superuser', False)
        )
        return self._insert_row(user)

    def filter_by_email(self, value: str):
        return self._db_session.query(self._user_model).filter(self._user_model.email == value).first()

    def filter_by_id(self, value: str):
        return self._db_session.query(self._user_model).filter(self._user_model.id == value).first()
