from flask import Blueprint
from src.interface_adapters.controllers.index.index_controller import IndexController

index_blueprint = Blueprint("index", __name__)

index_blueprint.add_url_rule(
    '/',
    view_func=IndexController.as_view("index"),
    methods=['GET']
)
