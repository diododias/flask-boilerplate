from sqlalchemy.dialects.postgresql import UUID
from src.resources.database import db

users_roles = db.Table(
    "users_roles",
    db.Column("user_id", UUID(as_uuid=True), db.ForeignKey("users.id")),
    db.Column("role_id", UUID(as_uuid=True), db.ForeignKey("roles.id")),
)
