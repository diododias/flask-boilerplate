import uuid

from datetime import datetime
from src.models.users_roles import users_roles
from sqlalchemy.dialects.postgresql import UUID
from src.resources.database import db
from src.resources.security import bcrypt


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String, index=True)
    last_name = db.Column(db.String, index=True)
    is_superuser = db.Column(db.Boolean(), default=False)
    roles = db.relationship(
        "Role", secondary=users_roles, back_populates="users"
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)

    def __init__(self, first_name, last_name, email, password, roles, is_superuser=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode()
        self.roles = roles
        self.is_superuser = is_superuser

    def __repr__(self):
        return f'<id: User: {self.email}>'





