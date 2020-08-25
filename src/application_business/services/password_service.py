from src.frameworks_and_drivers.security import bcrypt


class PasswordService:
    _encryptator: bcrypt

    def __init__(self, encrypt_engine: bcrypt):
        if encrypt_engine is None:
            raise Exception("Invalid encrypt engine")
        self._encryptator = encrypt_engine

    def check_password(self, saved_password, post_password) -> bool:
        """
        Validate password is correct
        :param saved_password: User password saved on db
        :param post_password: Password inserted by user to validate
        :return: A boolean indicating if password is correct
        """
        return self._encryptator.check_password_hash(
            saved_password, post_password
        )
