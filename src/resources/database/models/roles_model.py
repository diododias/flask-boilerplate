import uuid

from datetime import datetime
from src.resources.database import db
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from src.resources.database.models.users_roles_model import users_roles


class Role(db.Model):
    __tablename__ = "roles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, index=True)
    users = relationship("User", secondary=users_roles, back_populates="roles")
    created_at = Column(db.DateTime, default=datetime.utcnow(), index=True)

    def __init__(self, name: str):
        self.name = name
        self.created_at = datetime.now()
