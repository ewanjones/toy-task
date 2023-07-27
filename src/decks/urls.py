from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.GetDecks.as_view(), name="decks"),
    path("cards/create", views.AddCard.as_view(), name="add-card"),
]
