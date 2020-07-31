from src.interface_adapters.controllers.auth import auth_blueprint


def register_blueprints(app):
    app.register_blueprint(auth_blueprint)
