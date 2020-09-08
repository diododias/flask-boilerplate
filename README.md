# flask-boilerplate
`description english version coming`

Depois de desenvolver diversos projetos flask, eu pensei em criar um projeto que pudesse servir de base ou referência para qualquer tipo de aplicação, que seja fácil de expandir sem que seu crescimento se torne uma bagunça.

Seguindo boas praticas de desenvolvimento de API's e conceitos de Clean Architecture, esse projeto vai servir de referência para qualquer tipo de aplicação flask

### Requisitos

- Python 3.7+
- Docker

### Tecnologias

- Flask: Framework de desenvolvimento de API's Restful
- Docker: Infraestrutura entregue em containers
- Gunicorn: WSGI Server para disponibilizar a API Flask, configurado com gevent.
- Nginx: Proxy Reverso que serve como ponte de acesso a API e porta de entrada aos usuários.
- Marshmallow: Validação de valores enviados nas requisições
- Sqlalchemy: Framework de acesso ao banco de dados
- healthcheck: Healthcheck dos serviços de backend necessários para o funcionamento da API
- Swagger UI: Contrato de dados da API
- JWT: Mecanismo de autenticação
- Bcrypt: Encriptação de senhas
- Redis: Cache dos dados processados

## Iniciar a Aplicação

Toda aplicação foi desenvolvida para ser executado em containers

Inicie os containers com o comando abaixo

`docker-compose up -d`

#### Iniciar o banco de dados

A persistência de dados do postgres é realizada no diretório **docker/data-persistence**

A criação dos bancos de dados está no script **docker/init.sql** e é executada na inicialização do banco

O Comando abaixo vai criar as tabelas do banco seguindo o schema das entidades

`docker exec -it flask-api flask db init`

#### Aplicar migrações 

`docker exec -it flask-api flask db migrate`

#### Acessar o Swagger

URL: `http://localhost/swagger` 

#### Acessar o healthcheck

URL: `http://localhost/healthcheck`

## Qualidade de código

### test
`pytest --cov-report html:coverage/ --cov-report term-missing --cov-report xml:coverage/cov.xml --cov=src/ tests/`

### lint

`flake8`

### SonarQube check
Antes de executar o Sonar Scanner, crie um projeto e um token

Substitua o LOGIN_TOKEN no comando abaixo pelo token criado

`sonar-scanner  -Dsonar.projectKey=flask-boilerplate -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login="LOGIN_TOKEN" -Dsonar.exclusions=coverage/*,tests,migrations,docs,docker,coverage`

### Executar API em ambiente de desenvolvimento

`export FLASK_ENV=development`
`export FLASK_APP=wsgi.py`
`flask run`

## Clean Architecture

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

 





## TODO

- Expandir testes funcionais
- Alguns testes unitarios podem ser melhorados separados por cenários
- Pode ser incluso um endpoint para refresh do token
- Pode ser incluso um endpoint para CRUD das roles
- Pode ser incluso um endpoint para associar as roles ao usuário
- Pode ser incluso um endpoint para definir um usuário como administrador
- Melhorar README.me com versão em inglês, e explicar melhor a interação entre as camadas

 


