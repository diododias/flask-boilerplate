from src.resources.database import db


class RepositoryBase:
    """
    Interface to access database user model
    """
    _db_session: db.session

    def __init__(self, db_session: db.session):
        self._db_session = db_session

    def _insert_row(self, entity: db.Model):
        self._db_session.add(entity)
        self._db_session.commit()
        self._db_session.refresh(entity)
        return entity
