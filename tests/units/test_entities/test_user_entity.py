import uuid
from datetime import datetime
from src.enterprise_business.entities.user_entity import UserEntity


def test_user_entity_creation_and_values():
    user_id = uuid.uuid4()
    user = UserEntity(
        id=user_id,
        email="test@test.com",
        password="test",
        first_name="",
        last_name="",
        roles=list(),
        is_superuser=False,
        created_at=datetime.now(),
        cursor=None
    )

    assert user.id == user_id
    assert user.email == "test@test.com"
    assert user.password == "test"
    assert user.first_name == "" and isinstance(user.first_name, str)
    assert user.last_name == "" and isinstance(user.last_name, str)
