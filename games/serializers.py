from rest_framework import serializers

from .models import VideoGame, Video

class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                "title",
                "cover",
                "release_date",
                "imdb_rating",
                "certificate",
        )
        model = VideoGame
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video',)

class GameDetailSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = VideoGame
        fields = '__all__'
