import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

import pytest
from src.main import create_app


@pytest.fixture
def app():
    os.environ['APP_ENV'] = 'test'
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()
