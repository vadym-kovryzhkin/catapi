# Payload can be organized in different way. This is one of the most simple, but has its drawbacks
# In case if payload can be more complicated, the DTO pattern can be used. Read more about it here:
#   https://medium.com/@vadimkovrizhkin/design-services-to-work-with-rest-api-in-automation-tests-58b210ed6c34
from copy import deepcopy

_VOTE_PAYLOAD_TEMPLATE = {
    "image_id": "",
    "sub_id": "",
    "value": 1
}


def get_vote_payload():
    return deepcopy(_VOTE_PAYLOAD_TEMPLATE)
