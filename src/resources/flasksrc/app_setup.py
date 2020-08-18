from flask_cors import CORS
from swagger_ui import flask_api_doc

from src.resources.cache import cache
from src.resources.database import db
from src.resources.security import bcrypt
from src.resources.database import init_app as db_init_app
from src.resources.settings import settings_container, APP_ENV
from src.resources.flasksrc.register_blueprints import register_blueprints
from src.resources.database.repository.populate_initial_data import PopulateInitialData
from src.resources.flasksrc.error_handler import error_handler
from src.resources.resources_healthcheck.resources_healthcheck import init_app as healthcheck_init_app


def init_app(app):
    app.logger.info(f'Configure app in {APP_ENV} environment')
    app.config.from_object(settings_container.get(APP_ENV))
    flask_api_doc(app, config_path='./src/resources/swagger.json', url_prefix='/swagger',
                  title='Swagger from Flask Boilerplate')
    register_blueprints(app)
    cache.init_app(app)
    bcrypt.init_app(app)
    db_init_app(app)
    app.register_error_handler(400, error_handler)
    CORS(app, supports_credentials=True)
    healthcheck_init_app(app)

    @app.teardown_appcontext
    def shutdown_db_session(exception=None):
        db.session.remove()

    @app.before_first_request
    def setup():
        db_starter = PopulateInitialData(db_session=db.session)
        db_starter.start_populate()
