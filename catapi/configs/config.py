from os import getenv

from catapi.errors.configuration_errors import MissingEnvironmentVariable


def __get_env_value(var_name: str, default_value=None):
    value = getenv(var_name, default=default_value)
    if value is not None:
        return value
    raise MissingEnvironmentVariable(f"{var_name} has not been provided")


BASE_URL = __get_env_value("BASE_URL")
API_KEY = __get_env_value("API_KEY")
