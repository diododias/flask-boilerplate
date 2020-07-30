from src.resources.database import db
from src.resources.database.models.blacklist_token import BlacklistTokenModel
from src.resources.database.repository.blacklist_token_repository import BlacklistTokenRepository


class BlacklistTokenUseCase:
    _blacklist_token_model: type(BlacklistTokenModel)
    _blacklist_repository: type(BlacklistTokenRepository)

    def __init__(self, repository: BlacklistTokenRepository):
        self._blacklist_token_model = BlacklistTokenModel
        self._blacklist_repository = repository

    def check_blacklisted(self, auth_token):
        result = self._blacklist_repository.filter_by_token(auth_token)
        if result:
            return True
        else:
            return False

    def include_token_blacklist(self, auth_token):
        return self._blacklist_repository.create_blacklist_token(auth_token)
