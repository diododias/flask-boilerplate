# flask-boilerplate

export APP_ENV=development
export FLASK_ENV=development
docker-compose up -d
flask db init
flask db migrate
pytest --cov-report xml:coverage/coverage.xml --cov=src/ tests/

/Users/luizdiodo/Downloads/sonar-scanner-4.4.0.2170-macosx/bin/sonar-scanner  -Dsonar.projectKey=flask-boilerplate -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=06bdd2390fbd4bfe61fa60d5914fff2f779d89c5 -Dsonar.exclusions=coverage/*,tests,migrations,docs,docker,coverage






