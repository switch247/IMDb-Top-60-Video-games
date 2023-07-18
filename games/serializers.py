from rest_framework import serializers, permissions
from django.contrib.auth import get_user_model

from .models import VideoGame, Video, Review, Rating, WatchList, Photo, Trivia, Goof, Quote, FrequentlyAskedQuestion, ParentsGuide, Help

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
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo',)
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('review',)
class RatingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Rating
        fields = ('username', 'your_rating',)
    def to_representation(self, instance):
        if self.context['request'].user.is_authenticated:
            user = self.context['request'].user
            if instance.user == user:
                return super().to_representation(instance)
        return None
class WatchListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = WatchList
        fields = ('username', 'your_watchlist',)
    def to_representation(self, instance):
        if self.context['request'].user.is_authenticated:
            user = self.context['request'].user
            if instance.user == user:
                return super().to_representation(instance)
        return None

class TriviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trivia
        fields = ('trivia',)
class GoofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goof
        fields = ('goof',)
class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('quote',)
class FrequentlyAskedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestion
        fields = ('faq',)
class ParentsGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentsGuide
        fields = ('certification',)
class HelpListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('general_information',)


class GameDetailSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    class Meta:
        model = VideoGame
        fields = '__all__'
    reviews = ReviewSerializer(many=True, read_only=True)
    trivias = TriviaSerializer(many=True, read_only=True)
    goofs = GoofSerializer(many=True, read_only=True)
    quotes = QuoteSerializer(many=True, read_only=True)
    faqs = FrequentlyAskedQuestionSerializer(many=True, read_only=True)
    certificate = ParentsGuideSerializer(many=True, read_only=True)
class GameDetailSignedSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    watchlist = WatchListSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = VideoGame
        fields = '__all__'
        read_only_fields = ['title', 'cover', 'director', 'certificate', 'writer', 'award', 'storyline', 'genre', 'crazy_credits', 'soundtrack', 
                'country_of_origin', 'language', 'company', 'box_office', 'color', 'soundmix', 'nickname', 'release_date', 'popularity', 'metascore']
    reviews = ReviewSerializer(many=True, read_only=True)
    trivias = TriviaSerializer(many=True, read_only=True)
    goofs = GoofSerializer(many=True, read_only=True)
    quotes = QuoteSerializer(many=True, read_only=True)
    faqs = FrequentlyAskedQuestionSerializer(many=True, read_only=True)
    certificate = ParentsGuideSerializer(many=True, read_only=True)

class GameListSignedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                "title",
                "cover",
                "release_date",
                "imdb_rating",
                "certificate",
                "ratings",
                "watchlists",
        )
        model = VideoGame
