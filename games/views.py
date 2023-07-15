from rest_framework import generics

from .models import VideoGame
from .serializers import GameSerializer

# Create your views here.

class GameList(generics.ListCreateAPIView):
    queryset = VideoGame.objects.all()
    serializer_class = GameSerializer

class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoGame.objects.all()
    serializer_class = GameSerializer
