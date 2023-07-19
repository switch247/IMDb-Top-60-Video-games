from django.contrib import admin

# Register your models here.
from .models import VideoGame, Review, Video, Photo, Trivia, Goof, Quote, FrequentlyAskedQuestion, ParentsGuide, Rating, WatchList, Help, SoundTrack, Cast, CastVideo, CastPhoto 

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

class SoundTrackInLine(admin.StackedInline):
    model = SoundTrack

class CastPhotoInLine(admin.StackedInline):
    model = CastPhoto

class CastVideoInLine(admin.StackedInline):
    model = CastVideo

CastParentsGuideInLine

CastTriviaInLine

CastGoofInLine

CastQuoteInLine

CastFaqInLine


class CastInLine(admin.StackedInline):
    model = Cast

class CastAdmin(admin.ModelAdmin):
        inlines = [
            CastVideoInLine,
            CastPhotoInLine,
            CastParentsGuideInLine,
            CastTriviaInLine,
            CastGoofInLine,
            CastQuoteInLine,
            CastFaqInLine,
    ]
    list_display = ("name", "id", "cover", "born","game",)

class GameAdmin(admin.ModelAdmin):
    inlines = [
            WatchListInLine,
            RatingInLine,
            VideoInLine,
            PhotoInLine,
            CastInLine,
            ParentsGuideInLine,
            TriviaInLine,
            GoofInLine,
            QuoteInLine,
            SoundTrackInLine,
            ReviewInLine,
            FAQInLine,
    ]
    list_display = ("title","id", "cover","certificate", "release_date", "imdb_rating",)

admin.site.register(VideoGame, GameAdmin)
admin.site.register(Help)
admin.site.register(Cast, CastAdmin)
