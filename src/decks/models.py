from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=100)

    # Always protect FK relationships to prevent erroneous deletion.
    parent_deck = models.ForeignKey('self', related_name='child_decks', on_delete=models.PROTECT, null=True)
    # The order of the deck within its parent deck.
    parent_index = models.IntegerField(null=True)
    created_by = models.ForeignKey('auth.User', related_name='owned_decks', on_delete=models.PROTECT)
    users = models.ManyToManyField('auth.User', related_name='shared_decks')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'created_by')



class Card(models.Model):
    """
    One item in a deck.
    """
    deck = models.ForeignKey(Deck, related_name='cards', on_delete=models.CASCADE)

    # The position of the card within the deck>
    index = models.IntegerField()

    # The question/statement on the front of the card.
    front = models.TextField()
    # The answer or details on the back of the card.
    back = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('deck', 'front')
