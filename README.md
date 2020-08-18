# flask-boilerplate

- python3.7
- postgres
- sqlalchemy
- clean architecture

- docker-compose up -d
- export APP_ENV=development
- export FLASK_ENV=development
- flask db init
- flask db migrate
- flask run
- flake8
- pytest --cov-report html:coverage/ --cov-report term-missing --cov-report xml:coverage/cov.xml --cov=src/ tests/
- /Users/luizdiodo/Downloads/sonar-scanner-4.4.0.2170-macosx/bin/sonar-scanner  -Dsonar.projectKey=flask-boilerplate -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=06bdd2390fbd4bfe61fa60d5914fff2f779d89c5 -Dsonar.exclusions=coverage/*,tests,migrations,docs,docker,coverage






