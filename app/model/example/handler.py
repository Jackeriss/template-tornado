import logging

from schema import Optional, Use

from app.model.example.service import ExampleService
from app.util.handler_util import BasicHandler


class ExampleHandler(BasicHandler):
    async def get(self):
        result = await ExampleService.get_example()
        return self.success(result)
