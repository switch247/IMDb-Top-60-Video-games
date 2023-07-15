from rest_framework import serializers

from .models import VideoGame

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                "title",
                "cover",
                "director",
                "writer"
        )
        model = VideoGame
