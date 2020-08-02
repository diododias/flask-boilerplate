# flask-boilerplate

export APP_ENV=development
export FLASK_ENV=development
docker-compose up -d
flask db init
flask db migrate
pytest --cov-report xml:coverage/coverage.xml --cov=src/ tests/