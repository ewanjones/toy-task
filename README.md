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


## Notes

* I've used Django for this project because it's the framework I'm most familiar with.
* I think I misunderstood the instructions and called the app the wrong name before I started - I thought 
it was and application about toys
* I've split card content into front and back to prevent people from cheating by looking at the back of the card (or opening the network tab??)
* I ended up not going with the schema provided as it's easier to recreate using django migrations, and I added a few more fields to illustrate where I would go with this project


## Future work

* MySQL DB will do for now, but this should be postgres in a real project
* Typing got a bit rushed towards the end..
* More of the views required:
    * A view to create a deck
    * A view to update a card/deck - especially to edit `index`
    * A view to delete a card/deck
* I went for a RESTful approach, but I think GraphQL would be a good way to go for this project due 
  to the graphical nature of the data (sharing decks between users?)
