from django.urls import path

from .views import (
        GameList,
        GameDetail,
        HelpList,
        GameRate,
        GameWatchList,
        GameReview,
        SearchResultsListView,
        CastList,
        CastDetail,
        About,
        Contact,
)

urlpatterns = [
        path("", GameList.as_view(), name="game_list"),
        path("<uuid:pk>/", GameDetail.as_view(), name="game_detail"),
        path("<uuid:videogame_id>/casts/", CastList.as_view(), name="cast_list"),
        path("<uuid:videogame_id>/casts/<uuid:id>/", CastDetail.as_view(), name="cast_detail"),
        path("<uuid:videogame_id>/rating/", GameRate.as_view(), name="game_rating"),
        path("<uuid:videogame_id>/watchlist/", GameWatchList.as_view(), name="game_watchlist"),
        path("<uuid:videogame_id>/review/", GameReview.as_view(), name="game_review"),
        path("search/", SearchResultsListView.as_view(), name="search_results"),
        path("help/", HelpList.as_view(), name="help"),
        path("about/", About.as_view(), name="about"),
        path("contact/", Contact.as_view(), name="contact"),
]
