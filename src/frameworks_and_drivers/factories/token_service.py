from flask import request
from src.frameworks_and_drivers.database import db
from src.frameworks_and_drivers.database.repository.invalid_token_repository import InvalidTokenRepository
from src.application_business.services.token_service import TokenService
from src.frameworks_and_drivers.settings import settings_container, APP_ENV
from src.application_business.use_cases.filter_token_by_token_usecase import FilterTokenByTokenUseCase
from src.application_business.use_cases.invalidate_token_usecase import InvalidateTokenUseCase
from src.application_business.use_cases.create_token_entity_usecase import CreateTokenEntityUseCase
from src.application_business.use_cases.get_auth_token_usecase import GetAuthTokenUseCase


def create_token_service():
    token_repository = InvalidTokenRepository(db_session=db.session)
    return TokenService(create_token_entity_usecase=CreateTokenEntityUseCase(),
                        filter_token_by_token_usecase=FilterTokenByTokenUseCase(repository=token_repository),
                        invalidate_token_usecase=InvalidateTokenUseCase(repository=token_repository),
                        get_auth_token=GetAuthTokenUseCase(request=request),
                        secret=settings_container.get(APP_ENV).SECRET_KEY)
