from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


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
