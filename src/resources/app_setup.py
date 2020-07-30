from flask_cors import CORS
from swagger_ui import flask_api_doc

from src.controllers import register_blueprints
from src.frameworks_and_drivers.cache import cache
from src.frameworks_and_drivers.database import db
from src.frameworks_and_drivers.security import bcrypt
from src.frameworks_and_drivers.database import init_app as db_init_app
from src.frameworks_and_drivers.settings import settings_container, APP_ENV
from src.frameworks_and_drivers.database.populate_initial_data import populate_db


def init_app(app):
    app.logger.info(f'Configure app in {APP_ENV} environment')
    app.config.from_object(settings_container.get(APP_ENV))
    flask_api_doc(app, config_path='./src/frameworks_and_drivers/swagger.json', url_prefix='/',
                  title='Swagger from Flask Boilerplate')
    register_blueprints(app)
    cache.init_app(app)
    bcrypt.init_app(app)
    db_init_app(app)
    CORS(app, supports_credentials=True)

    @app.teardown_appcontext
    def shutdown_db_session(exception=None):
        db.session.remove()

    @app.before_first_request
    def setup():
        populate_db(db)
