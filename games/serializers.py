from rest_framework import serializers

from .models import VideoGame

class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                "title",
                "cover",
                "release_date",
                "imdb_rating",
                "parents_guide",
        )
        model = VideoGame
class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = VideoGame

