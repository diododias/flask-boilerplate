import uuid

from datetime import datetime
from src.resources.database import db
from sqlalchemy.dialects.postgresql import UUID
from src.resources.database.models.users_roles_model import users_roles


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String, index=True)
    users = db.relationship("User", secondary=users_roles, back_populates="roles")
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)

    def __init__(self, name: str, users):
        self.name = name
        self.users = users
        self.created_at = datetime.now()
