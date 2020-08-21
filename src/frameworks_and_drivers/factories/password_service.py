from src.frameworks_and_drivers.security import bcrypt
from src.application_business.services.password_service import PasswordService


def create_password_service():
    return PasswordService(encrypt_engine=bcrypt)
