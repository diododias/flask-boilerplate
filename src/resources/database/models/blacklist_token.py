import uuid

from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from src.resources.database import db


class BlacklistTokenModel(db.Model):
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
        return f'<id: token: {self.token}>'

