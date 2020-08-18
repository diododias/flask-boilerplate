from src.resources.database import db
from src.resources.database.models.users_model import User
from src.resources.database.models.roles_model import Role
from src.resources.database.repository.user_repository import UserRepository
from src.resources.database.repository.role_repository import RoleRepository
from src.resources.database.repository.repository_base import RepositoryBase
from src.resources.settings import settings_container, APP_ENV


class PopulateInitialData(RepositoryBase):
    def __init__(self, db_session: db.session):
        super().__init__(db_session)
        self._user_model = User
        self._role_model = Role
        self._user_repository = UserRepository(db_session)
        self._role_repository = RoleRepository(db_session)

    def start_populate(self):
        role = self._role_repository.filter_by_name("default")
        if not role:
            role = self._role_model(name="default")
            self._insert_row(role)

        user = self._user_repository.filter_by_email(settings_container.get(APP_ENV).FIRST_SUPERUSER)
        if not user:
            user = self._user_model(
                email=settings_container.get(APP_ENV).FIRST_SUPERUSER,
                password=settings_container.get(APP_ENV).FIRST_SUPERUSER_PASSWORD,
                first_name="default_first_name",
                last_name="default_last_name",
                roles=[role],
                is_superuser=True
            )
            self._insert_row(user)
