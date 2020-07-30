from datetime import datetime
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
from src.resources.database import db


@dataclass
class UserEntity:
    id: UUID(as_uuid=True)
    email: str
    password: str
    first_name: str
    last_name: str
    roles: list
    is_superuser: bool
    created_at: datetime
    cursor: db.Model
