from rest_framework import generics

from .models import VideoGame
from .serializers import GameListSerializer, GameDetailSerializer

# Create your views here.

class GameList(generics.ListCreateAPIView):
    queryset = VideoGame.objects.all()
    serializer_class = GameListSerializer

class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoGame.objects.all()
    serializer_class = GameDetailSerializer
