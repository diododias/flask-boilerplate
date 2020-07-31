import uuid

from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from src.resources.database.models.base_model import BaseModel
from src.resources.security import bcrypt
from src.resources.database.models.users_roles_model import users_roles


class Users(BaseModel):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    is_superuser = Column(Boolean(), default=False)
    roles = relationship(
        "Roles", secondary=users_roles, back_populates="users"
    )
    created_at = Column(DateTime, default=datetime.utcnow(), index=True)

    def __init__(self, first_name, last_name, email, password, roles, is_superuser=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode()
        self.roles = roles
        self.is_superuser = is_superuser

    def __repr__(self):
        return f'<id: User: {self.email}>'
