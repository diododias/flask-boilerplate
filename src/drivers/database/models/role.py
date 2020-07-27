from datetime import datetime
from src.drivers.database import db
from src.drivers.database.models.users_roles import users_roles


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    name = db.Column(db.String, index=True)
    users = db.relationship("User", secondary=users_roles, back_populates="roles")
