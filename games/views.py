from rest_framework import generics, permissions

from .models import VideoGame
from .serializers import GameListSerializer, GameDetailSerializer

# Create your views here.

class GameList(generics.ListAPIView):
    queryset = VideoGame.objects.all()
    serializer_class = GameListSerializer

class GameDetail(generics.ListAPIView):
    queryset = VideoGame.objects.all()
    serializer_class = GameDetailSerializer

class GameRate(generics.ListCreateAPIView):
    pass
