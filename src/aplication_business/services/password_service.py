from src.resources.security import bcrypt


class PasswordUseCase:
    _encryptator: bcrypt

    def __init__(self, encript_engine: bcrypt):
        if encript_engine is None:
            raise Exception("Invalid encrypt engine")
        self._encryptator = encript_engine

    def check_password(self, saved_password, post_password):
        return self._encryptator.check_password_hash(
            saved_password, post_password
        )
