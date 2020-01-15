import logging
from app.util.http_util import http_client
from app.constant import constant


class ExampleRpc:
    @classmethod
    async def get_example(cls):
        request_url = "https://api.bilibili.com/pgc/season/index/result"
        data = {
            "order": 5,
            "sort": 0,
            "pagesize": 20,
            "type": 1,
            "page": 1,
            "season_type": 1,
        }
        result = await http_client.get(request_url, params=data, response_format="json")
        if result.json_data.get("code") != 0:
            logging.error(f"response error: {result.json_data.get('code')}")
            return None
        return result.json_data.get("data", {})
