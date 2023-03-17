VOTE_SCHEMA_GET = {
    "type": "object",
    "properties": {
        "id": {"type": "number", "minimum": 1},
        "user_id": {"type": "string"},
        "image_id": {"type": "string"},
        "sub_id": {"type": "string"},
        "created_at": {"type": "string"},
        "value": {"type": "number"},
        "country_code": {"type": "string"},
        "image": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "url": {"type": "string"},
            },
            "required": ["id", "url"]
        },
    },
    "required": ["id", "user_id", "image_id", "sub_id", "created_at", "value", "country_code", "image"]
}

VOTE_SCHEMA_POST = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "id": {"type": "number", "minimum": 1},
    },
    "required": ["id", "message"]
}
