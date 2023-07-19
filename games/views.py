from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from .models import VideoGame, Help, Rating, WatchList, Review
from .serializers import GameListSerializer, GameDetailSerializer, HelpListSerializer, GameDetailSignedSerializer, GameListSignedSerializer, RatingSerializer, ReviewSerializer, WatchListSerializer

# Create your views here.

class GameList(generics.ListAPIView):
    queryset = VideoGame.objects.all()
    
    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return GameListSignedSerializer
        else:
            return GameListSerializer

class GameDetail(generics.RetrieveAPIView):
    queryset = VideoGame.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return GameDetailSignedSerializer
        else:
            return GameDetailSerializer

class GameRate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        game_id = self.kwargs['videogame_id']
        user = self.request.user
        try:
            rating = Rating.objects.get(game_id=game_id, user=user)
        except Rating.DoesNotExist:
            game = get_object_or_404(VideoGame, id=game_id)
            rating = Rating.objects.create(game=game, user=user)

        return rating
    def delete(self, request, *args, **kwargs):
        rating = self.get_object()
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class GameWatchList(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        game_id = self.kwargs['videogame_id']
        user = self.request.user

        try:
            watchlist = WatchList.objects.get(game_id=game_id, user=user)
        except WatchList.DoesNotExist:
            game = get_object_or_404(VideoGame, id=game_id)
            watchlist = WatchList.objects.create(game=game, user=user)

        return watchlist

class GameReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        game_id = self.kwargs['videogame_id']
        user = self.request.user

        try:
            review = Review.objects.get(game_id=game_id, user=user)
        except Review.DoesNotExist:
            game = get_object_or_404(VideoGame, id=game_id)
            review = Review.objects.create(game=game, user=user)

        return review

    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HelpList(generics.ListCreateAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpListSerializer

class SearchResultsListView(generics.ListAPIView):

    def get_queryset(self):
        queryset = VideoGame.objects.all()
        title = self.request.query_params.get('title', None)
        writer = self.request.query_params.get('writer', None)
        director = self.request.query_params.get('director', None)

        if title:
            queryset = queryset.filter(title__icontains=title)
        if writer:
            queryset = queryset.filter(writer__icontains=writer)
        if director:
            queryset = queryset.filter(director__icontains=director)

        return queryset

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return GameListSignedSerializer
        else:
            return GameListSerializer
