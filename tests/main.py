import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.main import create_app
from src.frameworks_and_drivers.settings import settings_container, APP_ENV


os.environ['APP_ENV'] = "test"

app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=os.environ.get('DEBUG', False), host="0.0.0.0", port=settings_container.get(APP_ENV).port)
