import pytest
import jsonschema

from catapi.json_schemas.vote_json_schema import VOTE_SCHEMA_GET
from catapi.json_schemas.vote_json_schema import VOTE_SCHEMA_POST
from catapi.payloads.votes import get_vote_payload


# we don't need a response of the created vote in the test, so we use the fixture with 'usefixtures'
@pytest.mark.usefixtures('created_vote')  # Arrange
def test_should_get_all_votes(authorized_cat_api_service_factory):
    # Act
    res = authorized_cat_api_service_factory.vote.get_all_votes()
    # Assert
    assert res.status_code == 200, "Could not get all votes"
    assert len(res.json()) > 0, "Response for getting all votes is empty"


def test_should_upvote_image(authorized_cat_api_service_factory, random_image_id, random_sub_id):
    # Arrange
    body = get_vote_payload()
    body["image_id"] = random_image_id
    body["sub_id"] = random_sub_id
    body["value"] = 1

    # Act
    res = authorized_cat_api_service_factory.vote.upvote_image(body)
    # Assert
    assert res.status_code == 201, "Could not create vote"
    jsonschema.validate(res.json(), VOTE_SCHEMA_POST)
    assert res.json()["message"] == "SUCCESS", "Vote response does not contain 'SUCCESS' message"
    assert res.json()["id"] > 0, "Vote 'id' property in the response is incorrect incorrect"


def test_should_get_already_created_vote(authorized_cat_api_service_factory, created_vote):
    # Arrange
    vote_id = created_vote["id"]

    # Act
    res = authorized_cat_api_service_factory.vote.get_vote_by_id(vote_id)

    # Assert
    assert res.status_code == 200, "Could not get vote by id"
    jsonschema.validate(res.json(), VOTE_SCHEMA_GET)
    assert res.json()["id"] == vote_id, "Vote 'id' property in the response is incorrect incorrect"


def test_should_delete_created_vote(authorized_cat_api_service_factory, created_vote):
    # Arrange
    vote_id = created_vote["id"]
    # Act
    res = authorized_cat_api_service_factory.vote.delete_vote_by_id(vote_id)

    # Assert
    assert res.status_code == 200, "Could not delete vote by id"
    assert res.json()["message"] == "SUCCESS", "Vote response does not contain 'SUCCESS' message"
