import pydantic
from django.contrib.auth.models import User

from decks import models


config = pydantic.ConfigDict(arbitrary_types_allowed=True)


class Card(pydantic.BaseModel):
    model_config = config

    deck_id: int
    index: int
    front: str
    back: str


class Deck(pydantic.BaseModel):
    model_config = config

    name: str
    # user ID
    # TODO: Make this a full user
    created_by: int
    cards: list[Card]

    @classmethod
    def from_model(cls, instance: models.Deck) -> "Deck":
        cards = instance.cards.all()
        serialised_cards = [
            Card(
                deck_id=instance.id, index=card.index, front=card.front, back=card.back
            ).model_dump()
            for card in cards
        ]
        serialised_cards.sort(key=lambda card: card["index"])

        return cls(
            name=instance.name,
            created_by=instance.created_by.id,
            cards=serialised_cards,
        )
