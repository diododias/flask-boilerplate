from healthcheck import HealthCheck, EnvironmentDump
from src.resources.resources_healthcheck.postgres import postgres_healthcheck
from src.resources.resources_healthcheck.redis import redis_healthcheck
from src.resources.resources_healthcheck.info import application_data


def init_app(app):
    health = HealthCheck(app, '/healthcheck')
    health.add_check(redis_healthcheck)
    health.add_check(postgres_healthcheck)
    envdump = EnvironmentDump(app, '/environment')
    envdump.add_section("application", application_data)
