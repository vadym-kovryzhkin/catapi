from catapi.api_services.base_api import BaseCatApiService
from catapi.routes.catapi_routes import CatApiRoutes


class CatVoteApiService(BaseCatApiService):

    def __init__(self):
        super().__init__()
        self._vote_route = CatApiRoutes.votes.value

    def upvote_image(self, body: dict):
        return self._post(body, self._vote_route)

    def get_all_votes(self):
        return self._get(self._vote_route)

    def get_vote_by_id(self, vote_id: int):
        return self._get(self._vote_route, vote_id)

    def delete_vote_by_id(self, vote_id: int):
        return self._delete(self._vote_route, vote_id)
