from catapi.api_services.base_api import Response


class ApiException(Exception):
    def __init__(self, message: str, response: Response):
        original_error = f"{message}. Original error: {response.status_code}, {response.text}"
        super().__init__(original_error)


class ApiCouldNotCreateVoteEntity(ApiException):
    pass


class ApiCouldNotGetImage(ApiException):
    pass
