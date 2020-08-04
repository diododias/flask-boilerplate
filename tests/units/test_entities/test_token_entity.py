import uuid
from datetime import datetime
from src.entities.token_entity import TokenEntity


def test_token_entity_creation_and_values():
    token_id = uuid.uuid4()
    token = TokenEntity(
        id=token_id,
        token="",
        blacklisted_on=datetime.now(),
        cursor=None
    )

    assert token.id == token_id
    assert token.token == ""
    assert isinstance(token.blacklisted_on, datetime)
