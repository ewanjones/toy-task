import pytest
from django.contrib.auth.models import User

from decks import models


@pytest.mark.django_db
def test_view_loads(authenticated_client):
    # TODO: tidy this up
    test_client, user = authenticated_client

    deck = models.Deck.objects.create(name="test", created_by=user)
    models.Card.objects.create(deck=deck, index=0, front="test-front", back="test-back")

    response = test_client.get("/decks/")

    assert response.status_code == 200
    assert response.json() == {
        "decks": [
            {
                "cards": [{"back": "test-back", "front": "test-front", "index": 0}],
                "created_by": 1,
                "name": "test",
            }
        ]
    }
