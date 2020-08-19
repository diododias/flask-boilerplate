from flask import Blueprint
from src.frameworks_and_drivers.database import db
from src.interface_adapters.controllers.index.index_controller import IndexController
from src.frameworks_and_drivers.database.repository.invalid_token_repository import InvalidTokenRepository


index_blueprint = Blueprint("index", __name__)

index_blueprint.add_url_rule(
    '/',
    view_func=IndexController.as_view("index", token_repository=InvalidTokenRepository(db_session=db.session)),
    methods=['GET']
)
