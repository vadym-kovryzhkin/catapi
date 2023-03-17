import random

import pytest

from catapi.api_services.cat_api_service_factory import CatApiServiceFactory
from catapi.configs import config
from catapi.errors.api_errors import ApiCouldNotCreateVoteEntity
from catapi.errors.api_errors import ApiCouldNotGetImage
from catapi.payloads.votes import get_vote_payload


@pytest.fixture()
def authorized_cat_api_service_factory() -> CatApiServiceFactory:
    cat_api_service_factory = CatApiServiceFactory()
    cat_api_service_factory.auth(config.API_KEY)
    return cat_api_service_factory


@pytest.fixture()
def unauthorized_cat_api_service_factory() -> CatApiServiceFactory:
    return CatApiServiceFactory()


# considering we are sure that there is always at least 1 image in the database
@pytest.fixture()
def random_image_id(authorized_cat_api_service_factory):
    """
    Get random image ID
    :return: image ID string
    """
    first_index = 0  # /images return list, and we just need to take any.
    res = authorized_cat_api_service_factory.image.search_random_image()
    if not res.ok:
        raise ApiCouldNotGetImage('Could not get random image', res)
    image_id = res.json()[first_index]['id']
    return image_id


@pytest.fixture()
def random_sub_id():
    """
    Generate random sub_id
    :return: number in string format
    """
    return str(random.randint(1000, 1000 * 5))


@pytest.fixture()
def created_vote(authorized_cat_api_service_factory, random_image_id, random_sub_id) -> dict:
    """
    Create vote (upvote image)
    :return: Vote response in dict format
    """
    body = get_vote_payload()
    body["image_id"] = random_image_id
    body["sub_id"] = random_sub_id
    body["value"] = 1
    upvoted_image_res = authorized_cat_api_service_factory.vote.upvote_image(body)
    if not upvoted_image_res.ok:
        raise ApiCouldNotCreateVoteEntity("Could not upvote image", upvoted_image_res)
    yield upvoted_image_res.json()
    authorized_cat_api_service_factory.vote.delete_vote_by_id(upvoted_image_res.json()["id"])
