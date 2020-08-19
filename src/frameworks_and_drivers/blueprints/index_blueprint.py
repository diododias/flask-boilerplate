from flask import Blueprint, request
from src.frameworks_and_drivers.database import db
from src.interface_adapters.controllers.index.index_controller import IndexController
from src.frameworks_and_drivers.database.repository.invalid_token_repository import InvalidTokenRepository
from src.application_business.services.token_service import TokenService
from src.frameworks_and_drivers.settings import settings_container, APP_ENV


index_blueprint = Blueprint("index", __name__)


index_blueprint.add_url_rule(
    '/',
    view_func=IndexController.as_view("index", TokenService(
        repository=InvalidTokenRepository(db_session=db.session),
        secret=settings_container.get(APP_ENV).SECRET_KEY,
        request=request
    )),
    methods=['GET']
)
