import uuid

from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from src.resources.database.models.users_roles import users_roles
from src.resources.database import db


class RoleModel(db.Model):
    __tablename__ = "roles"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    name = db.Column(db.String, index=True)
    users = db.relationship("UserModel", secondary=users_roles, back_populates="roles")

    def __repr__(self):
        return f'<id: role: {self.name}>'
