import uuid

from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from src.resources.database.models.base_model import BaseModel
from src.resources.database.models.users_roles_model import users_roles


class Roles(BaseModel):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), index=True)
    name = Column(String, index=True)
    users = relationship("Users", secondary=users_roles, back_populates="roles")

    def __repr__(self):
        return f'<id: role: {self.name}>'
