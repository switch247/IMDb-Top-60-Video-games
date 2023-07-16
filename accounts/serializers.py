from rest_framework import serializers
from games.serializers import GameListSerializer
from .models import IMDbUser
from games.models import WatchList, Rating, Review

class WatchListSerializer(serializers.ModelSerializer):
    game = GameListSerializer()
    class Meta:
        model = WatchList
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    game = GameListSerializer()
    class Meta:
        model = Rating
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    game = GameListSerializer()
    class Meta:
        model = Review
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMDbUser
        fields = ("cover", "username", "user_id", "bio", "nickname",)
