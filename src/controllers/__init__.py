from src.controllers.auth.auth_controller import auth_blueprint


def register_blueprints(app):
    app.register_blueprint(auth_blueprint)
