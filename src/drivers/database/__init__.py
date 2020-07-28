from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()
migrate = Migrate()


def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    migrate.init_app(app, db)

    @app.teardown_appcontext
    def shutdown_db_session(exception=None):
        db.session.remove()


def validate_uuid(uuid):
    try:
        uuid_obj = UUID(uuid)
        if uuid_obj:
            return True
        else:
            return False
    except ValueError:
        return False
