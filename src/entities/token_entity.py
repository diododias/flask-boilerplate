from datetime import datetime
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
from src.resources.database import db


@dataclass
class TokenEntity:
    id: UUID(as_uuid=True)
    token: str
    blacklisted_on: datetime
    cursor: db.Model
