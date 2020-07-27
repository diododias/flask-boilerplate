import datetime

from src.drivers.database import db
from hashlib import sha1


class Token(db.Model):
    """
    Token Model for storing JWT tokens
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    hash = db.Column(db.String(500), nullable=False)
    exp = db.Column(db.DateTime, nullable=False)
    iat = db.Column(db.DateTime, nullable=False)
    enabled = db.Column(db.Boolean, nullable=False)

    def __init__(self, hash):
        self.hash = str(sha1(hash.encode('utf-8')).hexdigest())
        self.iat = datetime.datetime.utcnow()
        self.exp = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        self.enabled = True

    @staticmethod
    def check_is_active(auth_token):
        res = Token.query.filter_by(hash=str(auth_token)).first()
        if res:
            return True
        else:
            return False
