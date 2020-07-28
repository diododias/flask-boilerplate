import uuid

from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from src.drivers.database import db
from src.drivers.database.models.users_roles import users_roles


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    name = db.Column(db.String, index=True)
    users = db.relationship("User", secondary=users_roles, back_populates="roles")
