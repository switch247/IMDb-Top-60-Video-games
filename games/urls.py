from django.urls import path

from .views import GameList, GameDetail, HelpList

urlpatterns = [
        path("", GameList.as_view(), name="game_list"),
        path("<uuid:pk>", GameDetail.as_view(), name="game_detail"),
        path("help", HelpList.as_view(), name="help"),
]
