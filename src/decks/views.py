import json

from django.http import HttpResponse
from django.views import View

from decks import models

from . import entities


class GetDecks(View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        decks = models.Deck.objects.filter()
        serialised_decks = list([entities.Deck.from_model(deck).model_dump() for deck in decks])

        return HttpResponse(
            json.dumps({"decks": serialised_decks}), content_type="application/json"
        )
