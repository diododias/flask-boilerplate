import os
import logging

from flask import Flask
from src.frameworks_and_drivers.flasksrc.app_setup import init_app
from src.frameworks_and_drivers.settings import settings_container, APP_ENV

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])
logger = logging.getLogger()


def create_app():
    app = Flask(__name__)
    init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=os.environ.get('DEBUG', False), host="0.0.0.0", port=settings_container.get(APP_ENV).port)
