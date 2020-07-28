import uuid

from datetime import datetime, timedelta
from sqlalchemy.dialects.postgresql import UUID
from src.drivers.database import db


class BlacklistToken(db.Model):
    """
    Token Model for storing Blacklisted JWT tokens
    """
    __tablename__ = "blacklist_tokens"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = str(token)
        self.blacklisted_on = datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklisted(auth_token):
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False
