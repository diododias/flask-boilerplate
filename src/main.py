import logging
import os

from flask import Flask
from src.drivers.rest.app_setup import init_app

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
    app.run(debug=os.environ.get('DEBUG', False), host="0.0.0.0", port=5000)
