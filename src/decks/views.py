import json

from django.http import HttpResponse
from django.views import View

from decks import models

from . import entities


class GetDecks(View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        if not request.user.is_authenticated:
            return HttpResponse(status=401)

        decks = models.Deck.objects.filter(created_by=request.user)
        serialised_decks = list([entities.Deck.from_model(deck).model_dump() for deck in decks])

        return HttpResponse(
            json.dumps({"decks": serialised_decks}), content_type="application/json"
        )
