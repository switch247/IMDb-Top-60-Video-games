from rest_framework import generics
from .models import IMDbUser
from games.models import WatchList, Rating, Review
from .serializers import WatchListSerializer, RatingSerializer, ReviewSerializer, AccountSerializer

class MyWatchList(generics.ListAPIView):
    serializer_class = WatchListSerializer
    
    def get_queryset(self):
        user_id = self.request.user.id
        return WatchList.objects.filter(user_id=user_id)

class MyRating(generics.ListAPIView):
    serializer_class = RatingSerializer
    
    def get_queryset(self):
        user_id = self.request.user.id
        return Rating.objects.filter(user_id=user_id)

class MyReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        user_id = self.request.user.id
        return Review.objects.filter(user_id=user_id)

class MyAccount(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = IMDbUser.objects.all()
