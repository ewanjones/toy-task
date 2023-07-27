import pytest
from django.contrib.auth.models import User

from decks import models


@pytest.mark.django_db
class TestGetDecks:
    def test_view_loads(self, authenticated_client):
        # TODO: tidy this up
        test_client, user = authenticated_client
        other_user = User.objects.create_user("Other Test", "test2@test.com", "testpassword")

        deck = models.Deck.objects.create(name="test", created_by=user)
        models.Card.objects.create(deck=deck, index=0, front="test-front", back="test-back")
        # Create a deck which should not be returned for this user
        models.Deck.objects.create(name="test", created_by=other_user)

        response = test_client.get("/decks/")

        assert response.status_code == 200
        assert response.json() == {
            "decks": [
                {
                    "cards": [
                        {
                            "back": "test-back",
                            "front": "test-front",
                            "index": 0,
                            "deck_id": deck.id,
                        }
                    ],
                    "created_by": 1,
                    "name": "test",
                }
            ]
        }

    def test_not_authenticated_return_405(self, test_client):
        user = User.objects.create_user("Test", "test@test.com", "testpassword")
        deck = models.Deck.objects.create(name="test", created_by=user)
        models.Card.objects.create(deck=deck, index=0, front="test-front", back="test-back")

        response = test_client.get("/decks/")

        assert response.status_code == 401


@pytest.mark.django_db
class TestAddCard:
    def test_add_card(self, authenticated_client):
        # TODO: tidy this up
        test_client, user = authenticated_client

        deck = models.Deck.objects.create(name="test", created_by=user)

        response = test_client.post(
            "/decks/cards/create",
        )

        assert response.status_code == 200
