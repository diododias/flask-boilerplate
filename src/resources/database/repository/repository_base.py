from src.resources.database import db


class RepositoryBase:
    """
    Interface to access database user model
    """
    _database_engine: db

    def __init__(self, database_engine: db):
        self._database_engine = database_engine

    def insert_row(self, entity: db.Model):
        self._database_engine.session.add(entity)
        self._database_engine.session.commit()
        self._database_engine.session.refresh(entity)
        return entity

    def remove_row(self, entity: db.Model):
        self._database_engine.session.delete(entity)
        self._database_engine.session.commit()


