import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.main import create_app
from src.resources.settings import settings_container, APP_ENV

app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=os.environ.get('DEBUG', False), host="0.0.0.0", port=settings_container.get(APP_ENV).port)
