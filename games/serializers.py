from rest_framework import serializers, permissions
from rest_framework.permissions import IsAuthenticated

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
    permission_classes = [IsAuthenticated]
    class Meta:
        model = Rating
        fields = ('your_rating',)
class WatchListSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]
    class Meta:
        model = WatchList
        permission_classes = [IsAuthenticated]
        fields = ('your_watchlist',)

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
    ratings = RatingSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    photos = PhotoSerializer
    class Meta:
        model = VideoGame
        fields = '__all__'
    reviews = ReviewSerializer(many=True, read_only=True)
    watchlists = WatchListSerializer(many=True, read_only=True)
    trivias = TriviaSerializer(many=True, read_only=True)
    goofs = GoofSerializer(many=True, read_only=True)
    quotes = QuoteSerializer(many=True, read_only=True)
    faqs = FrequentlyAskedQuestionSerializer(many=True, read_only=True)
    certificate = ParentsGuideSerializer(many=True, read_only=True)
