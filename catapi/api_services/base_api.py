from typing import Protocol

import requests

from catapi.configs import config


class Response(Protocol):
    ok: bool
    text: str
    status_code: int

    def json(self, **kwargs):
        pass


class BaseCatApiService:

    def __init__(self):
        self._base_url = config.BASE_URL
        self._session = requests.Session()

    def auth(self, api_key: str):
        self._session.headers.update({'x-api-key': api_key})
        return self

    def unauth(self):
        del self._session.headers['x-api-key']
        return self

    def _get(self, *routes, **kwargs) -> Response:
        url = self.__construct_url(*routes)
        return self._session.get(url, **kwargs)

    def _post(self, body: dict, *routes, **kwargs) -> Response:
        url = self.__construct_url(*routes)
        return self._session.post(url, json=body, **kwargs)

    def _delete(self, *routes, **kwargs) -> Response:
        url = self.__construct_url(*routes)
        return self._session.delete(url, **kwargs)

    def __construct_url(self, *routes):
        return self._base_url + "/" + "/".join(map(str, routes))
