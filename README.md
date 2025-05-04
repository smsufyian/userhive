# UserHive API

A simple FastAPI application that provides a "Hello World" API endpoint.

## Installation

This project uses Poetry for dependency management. To install the dependencies, run:

```bash
poetry install
```

## Running the API

To run the API, use the following command:

```bash
poetry run python -m src.userhive.app
```

Or you can use uvicorn directly:

```bash
poetry run uvicorn src.userhive.app:app --reload
```

The API will be available at http://localhost:8000.

## API Endpoints

### GET /

Returns a simple "Hello World" message.

**Response:**

```json
{
  "message": "helloworld"
}
```

## Development

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. The hooks perform the following tasks:
- Format code using Black
- Sort imports using isort
- Run linting using flake8
- Run tests using pytest

To install the pre-commit hooks, run:

```bash
poetry install
pre-commit install
```

The hooks will run automatically before each commit. If any hook fails, the commit will be aborted.

To run the hooks manually on all files:

```bash
pre-commit run --all-files
```

### Running Tests

To run the tests, use the following command:

```bash
poetry run pytest
```

### API Documentation

FastAPI automatically generates API documentation. When the API is running, you can access the documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
