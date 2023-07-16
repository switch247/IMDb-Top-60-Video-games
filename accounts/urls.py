from django.urls import path

from .views import MyWatchList, MyAccount, MyRating, MyReview

urlpatterns = [
        path("<uuid:pk>", MyAccount.as_view(), name="my_account"),
        path("<uuid:pk>/review", MyReview.as_view(), name="my_review"),
        path("<uuid:pk>/watchlist", MyWatchList.as_view(), name="my_watchlist"),
        path("<uuid:pk>/rating", MyRating.as_view(), name="my_rating"),
]
