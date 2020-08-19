import os

from src.main import create_app
from src.frameworks_and_drivers.settings import settings_container, APP_ENV


if __name__ == "__main__":
    app = create_app()
    app.run(debug=os.environ.get('DEBUG', False), host="0.0.0.0", port=settings_container.get(APP_ENV).port)
