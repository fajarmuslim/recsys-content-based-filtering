FROM python:3.10-slim

# Env variables
ENV ENV=staging \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.2.2 \
    PORT=8001

# Install gcc compiler since poetry depends on gcc
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    build-essential git libssl-dev libmariadb-dev libpq-dev && \
    pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Install deps
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

WORKDIR /app
COPY . /app

# This app run in port 8001
EXPOSE 8001

# Entry point to our app
ENTRYPOINT /usr/local/bin/uvicorn app.main:app --host 0.0.0.0 --port $PORT
