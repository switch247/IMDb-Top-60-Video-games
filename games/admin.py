from django.contrib import admin

# Register your models here.
from .models import VideoGame, Review

class ReviewInLine(admin.TabularInline):
    model = Review

class GameAdmin(admin.ModelAdmin):
    inlines = [
            ReviewInLine,
    ]
    list_display = ("title", "cover","certificate", "release_date",)

admin.site.register(VideoGame, GameAdmin)
