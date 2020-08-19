import os

from flask_cors import CORS
from swagger_ui import flask_api_doc
from src.frameworks_and_drivers.cache import cache
from src.frameworks_and_drivers.database import db
from src.frameworks_and_drivers.security import bcrypt
from src.frameworks_and_drivers.database import init_app as db_init_app
from src.frameworks_and_drivers.settings import settings_container, APP_ENV
from src.frameworks_and_drivers.flasksrc.register_blueprints import register_blueprints
from src.frameworks_and_drivers.database.repository.populate_initial_data import PopulateInitialData
from src.frameworks_and_drivers.flasksrc.error_handler import error_handler
from src.frameworks_and_drivers.healthchecks.healthchecks import init_app as healthcheck_init_app


def init_app(app):
    app.logger.info(f'Configure app in {APP_ENV} environment')
    app.config.from_object(settings_container.get(APP_ENV))
    flask_api_doc(app,
                  config_path=os.path.abspath(__file__).replace('flasksrc/app_setup.py', '') + 'swagger.json',
                  url_prefix='/swagger',
                  title='Swagger from Flask Boilerplate')
    cache.init_app(app)
    bcrypt.init_app(app)
    db_init_app(app)
    CORS(app, supports_credentials=True)
    healthcheck_init_app(app)
    register_blueprints(app)
    app.register_error_handler(500, error_handler)

    @app.teardown_appcontext
    def shutdown_db_session(exception=None):
        db.session.remove()

    @app.before_first_request
    def setup():
        db_starter = PopulateInitialData(db_session=db.session)
        db_starter.start_populate()
