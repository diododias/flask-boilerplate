from src.frameworks_and_drivers.database import db
from src.frameworks_and_drivers.factories.token_service import create_token_service
from src.frameworks_and_drivers.factories.password_service import create_password_service
from src.frameworks_and_drivers.database.repository.user_repository import UserRepository
from src.application_business.services.user_service import UserService
from src.application_business.use_cases.create_user_usecase import CreateUserUseCase
from src.application_business.use_cases.create_user_entity_usecase import CreateUserEntityUseCase
from src.application_business.use_cases.filter_user_by_id_usecase import FilterUserByIdUseCase
from src.application_business.use_cases.filter_user_by_email_usecase import FilterUserByEmailUseCase


def create_user_service():
    user_repository = UserRepository(db_session=db.session)
    return UserService(create_user_usecase=CreateUserUseCase(repository=user_repository),
                       filter_user_by_email_usecase=FilterUserByEmailUseCase(repository=user_repository),
                       filter_user_by_id_usecase=FilterUserByIdUseCase(repository=user_repository),
                       create_user_entity_usecase=CreateUserEntityUseCase(),
                       token_service=create_token_service(),
                       password_service=create_password_service())
