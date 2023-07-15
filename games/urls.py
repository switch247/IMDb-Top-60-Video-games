from django.urls import path

from .views import GameList, GameDetailView

urlpatterns = [
        path("", GameList.as_view(), name="game_list"),
        path("<uuid:pk>", GameDetailView.as_view(), name="game_detail"),
]
