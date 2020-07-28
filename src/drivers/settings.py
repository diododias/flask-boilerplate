import os

APP_ENV = os.environ.get('APP_ENV', 'production')


class BaseConfig(object):
   FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
   API_PREFIX = '/'
   CACHE_TYPE = 'redis'
   CACHE_REDIS_URL = 'redis://localhost:6379/0'
   CACHE_DEFAULT_TIMEOUT = 300
   TESTING = False
   FLASK_DEBUG = os.environ.get('FLASK_DEBUG', False)
   APP_DIR = os.path.abspath(os.path.dirname(__file__))
   PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
   CSRF_ENABLED = True
   SECRET_KEY = os.environ.get('SECRET_KEY', '7311a881f138d32a94994cef3e4b855e')
   POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
   POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
   POSTGRES_URL = os.environ.get('POSTGRES_URL', 'localhost:5432')
   POSTGRES_DB = os.environ.get('POSTGRES_DB', 'flask-base')
   DB_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_URL}/{POSTGRES_DB}'
   SQLALCHEMY_DATABASE_URI = DB_URL
   SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
   FIRST_SUPERUSER = os.environ.get('FIRST_SUPERUSER', 'diodo')
   FIRST_SUPERUSER_PASSWORD = os.environ.get('FIRST_SUPERUSER_PASSWORD', 'diodex777')


class DevConfig(BaseConfig):
   FLASK_ENV = 'development'
   ENV = FLASK_ENV
   SQLALCHEMY_ECHO = False
   DEBUG = True


class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'
   ENV = FLASK_ENV


class TestConfig(BaseConfig):
   FLASK_ENV = 'test'
   ENV = FLASK_ENV
   TESTING = True
   DEBUG = True


settings_container = {
   "development": DevConfig,
   "production": ProductionConfig,
   "test": TestConfig
}