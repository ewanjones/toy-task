# Toys

## Installation

Create and activate a Python 3.11 virtual environment using poetry:

```sh
pip install poetry
poetry env use 3.11.4
poetry install
```

Run migrations using:

```sh
poetry run src/python manage.py migrate
```

This will create a SQLite database in the src/ directory (I won't make you set up a postgres for 
this, but I would do this in a real project).


## Testing and linting

Run the test suite with:

```sh
poetry run pytest
```

Run mypy with:

```sh
poetry run mypy
```

Run flake 8 with:

```sh
poetry run flake8
```
