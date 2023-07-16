from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import IMDbUserCreationForm, IMDbUserChangeForm
from .models import IMDbUser
from games.models import Review, WatchList, Rating
import uuid

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review

class WatchListInline(admin.TabularInline):
    model = WatchList

class RatingInline(admin.TabularInline):
    model = Rating

class IMDbUserAdmin(UserAdmin):
    add_form = IMDbUserCreationForm
    form = IMDbUserChangeForm
    model = IMDbUser
    list_display = [
            "username",
            "email",
            "bio",
            "user_id",
            "cover",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("nickname", "user_id", "bio", "cover" ,)}),)
    addfieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("nickname", "user_id","bio", "cover",)}),)
    inlines = [ReviewInline, RatingInline, WatchListInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return super().get_inline_instances(request, obj)
        else:
            return [
                    inline(self.model, self.admin_site)
                    for inline in self.inlines
                    if inline.model (Review, Rating, WatchList) and hasattr(inline, 'get_queryset')
            ]

admin.site.register(IMDbUser, IMDbUserAdmin)
