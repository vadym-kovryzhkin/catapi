# The Cat API automation framework sample for REST API automation tests
#### Example of test automation API framework based on https://thecatapi.com/ website


# Usage

## Configuration
This step is a must
1. Receive API key from https://thecatapi.com/ (Free)
1. Set next env variables in terminal: 
   ```
   export BASE_URL=https://api.thecatapi.com/v1
   export API_KEY="you api key from step 1"
   ```


## Docker execution
### Requirements
1. Install Docker: https://www.docker.com/

### Tests Execution
1. Make sure 'Configuration' step is done
1. Build Docker image: `docker build -t framework-sample .`
1. Run tests inside Docker container: `docker run --name tests --rm -e BASE_URL=$BASE_URL -e API_KEY=$API_KEY framework-sample`

## Development environment
### Requirements 
1. Install Python 3.9+
1. Install poetry: https://python-poetry.org/docs/

### Tests execution
1. Make sure 'Configuration' step is done
1. Set Poetry virtualenv setup in the project folder: `poetry config virtualenvs.in-project true`
1. Install poetry dependencies: `poetry install`
1. Activate virtualenv: `poetry shell`
1. Run tests: `poetry run pytest` 
1. Run tests with DEBUG: `poetry run pytest -v --log-cli-level=DEBUG -s`


### What else can be improved
1. .env usage
1. Logs
1. Dockerfile optimization and configuration (CMD command)
1. Tests execution command (e.g. using bash)
1. Test data arrangement
1. Non *unix support
</br> 
etc...