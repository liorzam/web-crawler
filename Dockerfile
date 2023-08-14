# Use a base image with Python pre-installed
FROM python:3.9.13-slim-buster AS builder

WORKDIR /app

# Copy the poetry.lock and pyproject.toml files to the builder stage
COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

# Install project dependencies using Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /app

# Specify the command to run when the container starts
ENTRYPOINT ["python",  "main.py"]