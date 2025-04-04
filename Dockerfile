FROM python:3.11.4-slim-buster AS base

WORKDIR /src

COPY pyproject.toml README.md  .
RUN pip install poetry

FROM base AS dependencies
RUN poetry install --no-dev

FROM base AS development
COPY . .
RUN poetry install

FROM dependencies AS production
COPY src src
COPY logging.conf src
