from django.contrib import admin

# Register your models here.
from .models import VideoGame, Review, Video, Photo, Trivia, Goof, Quote, FrequentlyAskedQuestion, ParentsGuide, Rating, WatchList, Help

class WatchListInLine(admin.TabularInline):
    model = WatchList

class RatingInLine(admin.TabularInline):
    model = Rating

class ReviewInLine(admin.TabularInline):
    model = Review

class PhotoInLine(admin.TabularInline):
    model = Photo

class TriviaInLine(admin.TabularInline):
    model = Trivia

class GoofInLine(admin.TabularInline):
    model = Goof

class QuoteInLine(admin.TabularInline):
    model = Quote

class FAQInLine(admin.TabularInline):
    model = FrequentlyAskedQuestion

class ParentsGuideInLine(admin.StackedInline):
    model = ParentsGuide

class VideoInLine(admin.StackedInline):
    model = Video

class GameAdmin(admin.ModelAdmin):
    inlines = [
            ReviewInLine, VideoInLine, ParentsGuideInLine, FAQInLine, QuoteInLine, GoofInLine, TriviaInLine, PhotoInLine, WatchListInLine, RatingInLine
    ]
    list_display = ("title","id", "cover","certificate", "release_date", "imdb_rating",)

admin.site.register(VideoGame, GameAdmin)
admin.site.register(Help)
