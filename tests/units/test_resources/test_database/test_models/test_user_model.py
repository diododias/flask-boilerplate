from src.resources.database.models.users_model import User


def test_user_model_creation_and_values():
    user = User(
        email="test@test.com",
        password="test",
        first_name="",
        last_name="",
        roles=[],
        is_superuser=False
    )
    assert user is not None
