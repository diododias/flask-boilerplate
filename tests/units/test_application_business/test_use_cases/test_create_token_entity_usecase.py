from mock import MagicMock
from src.frameworks_and_drivers.database import db
from src.application_business.use_cases.crete_token_entity_usecase import CreateTokenEntityUseCase
from src.enterprise_business.entities.token_entity import TokenEntity


def test_create_token_entity_ok():
    usecase = CreateTokenEntityUseCase()

    db_model = MagicMock(spec=db.Model)
    db_model.id = "id"
    db_model.token = "token"
    db_model.blacklisted = ""
    entity = usecase.execute(db_model)

    assert isinstance(entity, TokenEntity)
    assert entity.id == "id"
    assert entity.token == "token"

