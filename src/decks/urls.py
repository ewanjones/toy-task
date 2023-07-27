from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.GetDecks.as_view(), name="decks")
]
