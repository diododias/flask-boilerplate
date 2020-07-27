from datetime import datetime
from src.drivers.database import db
from src.drivers.database.models.users_roles import users_roles
from src.drivers.security import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    first_name = db.Column(db.String, index=True)
    last_name = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    is_active = db.Column(db.Boolean(), default=True)
    is_superuser = db.Column(db.Boolean(), default=False)
    roles = db.relationship(
        "Role", secondary=users_roles, back_populates="users"
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = bcrypt.generate_password_hash(kwargs.get('password')).decode()



