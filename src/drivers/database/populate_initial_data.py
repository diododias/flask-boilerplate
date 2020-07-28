from src.drivers.database import db
from src.drivers.database.models.user import User
from src.drivers.database.models.role import Role


def populate_db():
    role = Role.query.filter_by(name="default").first()
    if not role:
        role = Role(name="default")
        db.session.add(role)
        db.session.commit()
        db.session.refresh(role)

    user = User.query.filter_by(email="default").first()
    if not user:
        user = User(email="default",
                    password="admin@123",
                    first_name="default_first_name",
                    last_name="default_last_name",
                    roles=[role],
                    is_superuser=False)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        user.roles.append(role)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
