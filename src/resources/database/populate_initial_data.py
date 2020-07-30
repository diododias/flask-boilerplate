from src.resources.database.models.user import UserModel
from src.resources.database.models.role import RoleModel
from src.resources.database.repository.repository_base import RepositoryBase
from src.resources.settings import settings_container, APP_ENV


class PopulateInitialData(RepositoryBase):

    def start_populate(self):
        role = RoleModel.query.filter_by(name="default").first()
        if not role:
            role = RoleModel(name="default")
            self.insert_row(role)

        user = UserModel.query.filter_by(email=settings_container.get(APP_ENV).FIRST_SUPERUSER).first()
        if not user:
            user = UserModel(email=settings_container.get(APP_ENV).FIRST_SUPERUSER,
                             password=settings_container.get(APP_ENV).FIRST_SUPERUSER_PASSWORD,
                             first_name="default_first_name",
                             last_name="default_last_name",
                             roles=[role],
                             is_superuser=True)
            self.insert_row(user)
            user.roles.append(role)
            self.insert_row(user)
