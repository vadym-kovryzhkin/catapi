from catapi.api_services.base_api import BaseCatApiService
from catapi.routes.catapi_routes import CatApiRoutes


class CatImageApiService(BaseCatApiService):

    def __init__(self):
        super().__init__()
        self._image_route = CatApiRoutes.images.value

    def search_random_image(self):
        return self._get(CatApiRoutes.images.value, CatApiRoutes.search.value)
