from src.frameworks_and_drivers.database import db
from src.frameworks_and_drivers.database.models.roles_model import Role
from src.frameworks_and_drivers.database.repository.repository_base import RepositoryBase


class RoleRepository(RepositoryBase):
    def __init__(self, db_session: db.session):
        super().__init__(db_session)
        self._role_model = Role

    def filter_by_name(self, value: str):
        return self._db_session.query(self._role_model).filter(self._role_model.name == value).first()

    def filter_by_id(self, value: str):
        return self._db_session.query(self._role_model).filter(self._role_model.id == value).first()
