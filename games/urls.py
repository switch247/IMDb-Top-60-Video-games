from django.urls import path

from .views import GameList, GameDetail, HelpList, GameRate, GameWatchList, GameReview

urlpatterns = [
        path("", GameList.as_view(), name="game_list"),
        path("<uuid:pk>", GameDetail.as_view(), name="game_detail"),
        path("<uuid:game_id>/rating", GameRate.as_view(), name="game_rating"),
        path("<uuid:game_id>/watchlist", GameWatchList.as_view(), name="game_watchlist"),
        path("<uuid:game_id>/review", GameReview.as_view(), name="game_review"),
        path("help", HelpList.as_view(), name="help"),
]
