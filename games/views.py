from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from .models import VideoGame, Help, Rating
from .serializers import GameListSerializer, GameDetailSerializer, HelpListSerializer, GameDetailSignedSerializer, GameListSignedSerializer, RatingSerializer, RateSerializer

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
class GameRate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VideoGame.objects.all()
    serializer_class = RateSerializer

class HelpList(generics.ListCreateAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpListSerializer
