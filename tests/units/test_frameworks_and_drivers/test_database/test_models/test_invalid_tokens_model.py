import uuid
from src.frameworks_and_drivers.database.models.invalid_tokens_model import InvalidToken


def test_invalid_tokens_model_creation_and_values():
    token = InvalidToken(token=uuid.uuid4())
    assert token is not None
