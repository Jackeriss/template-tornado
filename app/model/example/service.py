import time
import asyncio

from app.model.example.rpc import ExampleRpc
from app.util.time_util import timeout_log
from app.util.cache_util import cache


class ExampleService:
    @classmethod
    @timeout_log(timeout=5)
    @cache(expire=3, storage="redis")
    async def get_example(cls):
        example = await ExampleRpc.get_example()
        if not example:
            return {
                "example": {},
            }
        result = {
            "example": example,
        }
        return result
