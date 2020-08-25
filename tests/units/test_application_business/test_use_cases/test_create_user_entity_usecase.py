from mock import MagicMock
from src.frameworks_and_drivers.database import db
from src.application_business.use_cases.create_user_entity_usecase import CreateUserEntityUseCase
from src.enterprise_business.entities.user_entity import UserEntity


def test_create_user_entity_ok():
    usecase = CreateUserEntityUseCase()

    db_model = MagicMock(spec=type(db.Model))
    db_model.id = "id"
    db_model.email = "email"
    db_model.first_name = "first_name"
    db_model.last_name = "last_name"
    db_model.password = "password"
    db_model.roles = list()
    db_model.is_superuser = False
    db_model.created_at = ""

    entity = usecase.execute(db_model)

    assert isinstance(entity, UserEntity)
    assert entity.id == "id"
    assert entity.email == "email"


def test_create_user_entity_invalid_input():
    usecase = CreateUserEntityUseCase()

    result = usecase.execute("")
    assert isinstance(result, str)

    result = usecase.execute(None)
    assert result is None

    result = usecase.execute(123)
    assert isinstance(result, int)
