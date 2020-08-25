# flask-boilerplate
`description english version coming`

Este projeto é o resultado de um estudo em desenvolvimento de APIs Restful baseado em Flask

O objetivo foi desenvolver um repositório que sirva de base para qualquer projeto Flask, sua arquitetura precisa facilitar o crescimento robusto sem impactos na sua estrutura.
deve ser fácil de dar manutenção e simples de compreender

Sua arquitetura segue os conceitos do Clean Architecture


### Clean Architecture

Esse projeto foi desenvolvido seguindo os conceitos do Clean Architecture / Arquitetura Hexagonal
cada componente foi desenvolvido de forma isolada, minimizando ao máximo o acoplamento

O nivel de dependencia das camadas vai de cima para baixo, onde a camada de cima conhece a de baixo mas a de baixo não conhece a de cima,
as dependencias são injetadas na construção das classes

- Frameworks and Drivers
- Interface Adapters
- Application Business
- Enterprise Business

### Camadas

#### Frameworks and Drivers

Essa camada é responsável pela infra estrutura e construção das classes dos niveis abaixo dela

#### Interface Adapters

Nessa camada é implementado os controllers, responsável por definir os endpoints da API e chamar o serviço

#### Application Business

##### Casos de Uso

Nessa camada é implementado o caso de uso. 
Cada caso de uso é uma parte minima responsável por apenas uma tarefa, os casos de uso são utilizados pelos serviços.


##### Serviços

Nessa camada é implementado o serviço fornecido pelos endpoints, onde é o ponto central da logica do negócio,
utiliza dos casos de uso como dependencia para implementação dos algoritimos de serviço

 
### Requisitos

- python3.7+
- redis
- postgres

### Tecnologias

- marshmallow
- sqlalchemy
- healthcheck
- swagger ui
- docker
- gunicorn
- nginx
- supervisor


### Start infrastructure

docker-compose up -d

### create database

#instructions

### Init database schemas

flask db init
flask db migrate

### test
pytest --cov-report html:coverage/ --cov-report term-missing --cov-report xml:coverage/cov.xml --cov=src/ tests/

### lint

flake8

### SonarQube check

sonar-scanner  -Dsonar.projectKey=flask-boilerplate -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login="LOGIN_TOKEN" -Dsonar.exclusions=coverage/*,tests,migrations,docs,docker,coverage

### Run API in development environment

export APP_ENV=development
export FLASK_ENV=development
export FLASK_APP=wsgi.py
flask run

## TODO

- Expandir testes funcionais
- Alguns testes unitarios podem ser melhorados separados por cenários
- Pode ser incluso um endpoint para refresh do token
- Pode ser incluso um endpoint para CRUD das roles
- Pode ser incluso um endpoint para associar as roles ao usuário
- Pode ser incluso um endpoint para definir um usuário como administrador
- Melhorar README.me com versão em inglês, e explicar melhor a interação entre as camadas

 


