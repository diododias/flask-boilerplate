from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

users_roles = Table(
    "users_roles",
    Base.metadata,
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True),
    Column("role_id", UUID(as_uuid=True), ForeignKey("roles.id"), primary_key=True),
)
