from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from .models import VideoGame, Help, Rating
from .serializers import GameListSerializer, GameDetailSerializer, HelpListSerializer, RatingSerializer

# Create your views here.

class GameSigned(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer(many=True, read_only=True)

class GameList(generics.ListAPIView):
    queryset = VideoGame.objects.all()
    serializer_class = GameListSerializer

class GameDetail(generics.RetrieveAPIView):
    queryset = VideoGame.objects.all()
    serializer_class = GameDetailSerializer
    my_ratings = GameSigned.as_view()

class HelpList(generics.ListCreateAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpListSerializer
