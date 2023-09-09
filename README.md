# FastAPI template

requirements: `docker`, `docker-compose` and `poetry` (for tests)

# Usage

Create an `.env` file based on `.env.template`.

For development: `docker-compose up`

For production: `docker-compose -f docker-compose.prod.yaml up`

# Tests

`poetry run pytest main.py`
