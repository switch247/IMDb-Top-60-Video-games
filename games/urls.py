from django.urls import path

from .views import GameList, GameDetail

urlpatterns = [
        path("", GameList.as_view(), name="game_list"),
        path("<uuid:pk>", GameDetail.as_view(), name="game_detail"),
]
