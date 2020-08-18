from src.resources.cache import cache


def redis_healthcheck():
    cache_ok = cache.set('healthcheck', 'ok', 30)

    if cache_ok:
        return True, "redis ok"
    else:
        return False, "redis not ok"
