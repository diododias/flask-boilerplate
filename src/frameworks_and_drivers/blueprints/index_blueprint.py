from flask import Blueprint, request
from src.interface_adapters.controllers.index.index_controller import IndexController
from src.frameworks_and_drivers.factories.token_service import create_token_service


index_blueprint = Blueprint("index", __name__)


index_blueprint.add_url_rule(
    '/',
    view_func=IndexController.as_view("index", token_service=create_token_service(), flask_request=request),
    methods=['GET']
)
