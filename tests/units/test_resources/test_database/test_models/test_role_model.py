from src.resources.database.models.roles_model import Role


def test_role_model_creation_and_values():
    role = Role(name="default", users=list())
    assert role is not None
