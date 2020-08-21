from src.frameworks_and_drivers.database import db
from src.application_business.interfaces.base_repository import IBaseRepository


class RepositoryBase(IBaseRepository):
    """
    Interface to access database user model
    """

    def __init__(self, db_session: db.session):
        self._db_session = db_session

    def _insert_row(self, entity: db.Model) -> db.Model:
        self._db_session.add(entity)
        self._db_session.commit()
        self._db_session.refresh(entity)
        return entity
