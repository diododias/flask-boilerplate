from swagger_ui import flask_api_doc
from flask_cors import CORS
from src.controllers import register_blueprints
from src.drivers.cache import cache
from src.drivers.settings import settings_container, APP_ENV
from src.drivers.security import init_app as bcrypt_init_app
from src.drivers.database import init_app as db_init_app, db
from src.drivers.database.populate_initial_data import populate_db


def init_app(app):
    app.logger.info(f'Configure app in {APP_ENV} environment')
    app.config.from_object(settings_container.get(APP_ENV))
    flask_api_doc(app, config_path='./src/drivers/rest/swagger.json', url_prefix='/swagger',
                  title='Swagger from Flask Boilerplate')
    register_blueprints(app)
    cache.init_app(app)
    bcrypt_init_app(app)
    db_init_app(app)
    CORS(app, supports_credentials=True)

    @app.teardown_appcontext
    def shutdown_db_session(exception=None):
        db.session.remove()

    @app.before_first_request
    def setup():
        populate_db()
