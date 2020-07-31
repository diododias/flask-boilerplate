import uuid

from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from src.resources.database.models.base_model import BaseModel


class InvalidTokens(BaseModel):
    """
    Token Model for storing Blacklisted JWT tokens
    """
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    token = Column(String(500), unique=True, nullable=False)
    blacklisted_on = Column(DateTime, nullable=False)

    def __init__(self, token):
        self.token = str(token)
        self.blacklisted_on = datetime.now()

    def __repr__(self):
        return f'<id: token: {self.token}>'
