from app.util.config_util import config


redis_pool = None  # type: aioredis.Pool


async def init_redis_pool(loop):
    import aioredis

    global redis_pool
    address, redis_config = config.redis
    redis_pool = await aioredis.create_redis_pool(address, loop=loop, **redis_config)
