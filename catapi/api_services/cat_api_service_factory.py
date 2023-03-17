"""
Factory Method Pattern implementation, with the possibility to auth service providing API KEY.
----
Usage example:
```
cat_api_service = CatApiServiceFactory()
cat_api_service.auth()
cat_api_service.image.search_random_image()
cat_api_service.vote.get_all_votes()
```
"""
from catapi.api_services.base_api import BaseCatApiService
from catapi.api_services.image_api_service import CatImageApiService
from catapi.api_services.vote_api_service import CatVoteApiService


class CatApiServiceFactory:
    def __init__(self):
        super().__init__()
        self.__api_key = None

    def __authorize_service(self, service: BaseCatApiService):
        if self.__api_key:
            service.auth(self.__api_key)

    def auth(self, api_key):
        self.__api_key = api_key
        return self

    @property
    def image(self):
        service = CatImageApiService()
        self.__authorize_service(service)
        return service

    @property
    def vote(self):
        service = CatVoteApiService()
        self.__authorize_service(service)
        return service
