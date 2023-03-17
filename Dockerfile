FROM python:3.10.8

RUN mkdir -p /app

RUN apt-get update

RUN pip install poetry
COPY pyproject.toml /app
COPY poetry.lock /app

RUN set -x \
    && cd /app \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi --no-root

WORKDIR /app
COPY . /app

CMD [ "poetry", "run", "pytest"]