from mock import MagicMock
from src.frameworks_and_drivers.database import db
from src.application_business.use_cases.create_token_entity_usecase import CreateTokenEntityUseCase
from src.enterprise_business.entities.token_entity import TokenEntity


def test_create_token_entity_ok():
    usecase = CreateTokenEntityUseCase()

    db_model = MagicMock(spec=type(db.Model))
    db_model.id = "id"
    db_model.token = "token"
    db_model.blacklisted_on = ""
    entity = usecase.execute(db_model)

    assert isinstance(entity, TokenEntity)
    assert entity.id == "id"
    assert entity.token == "token"


def test_create_token_entity_invalid_input():
    usecase = CreateTokenEntityUseCase()

    result = usecase.execute("")
    assert isinstance(result, str)

    result = usecase.execute(None)
    assert result is None

    result = usecase.execute(123)
    assert isinstance(result, int)
