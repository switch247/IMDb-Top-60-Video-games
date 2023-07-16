from django.contrib import admin

# Register your models here.
from .models import VideoGame, Review, Video

class ReviewInLine(admin.TabularInline):
    model = Review

class VideoInLine(admin.StackedInline):
    model = Video

class GameAdmin(admin.ModelAdmin):
    inlines = [
            ReviewInLine, VideoInLine
    ]
    list_display = ("title", "cover","certificate", "release_date",)

admin.site.register(VideoGame, GameAdmin)
