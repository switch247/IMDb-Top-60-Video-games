from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import IMDbUserCreationForm, IMDbUserChangeForm
from .models import IMDbUser

# Register your models here.

class IMDbUserAdmin(UserAdmin):
    add_form = IMDbUserCreationForm
    form = IMDbUserChangeForm
    model = IMDbUser
    list_display = [
            "name",
            "my_review",
            "my_rating",
            "bio",
            "user_id",
            "cover",
            "my_watchlist",
            ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name", "user_id", "my_rating","bio", "cover", "my_review",)}),)
    addfieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name", "user_id", "my_rating","bio", "cover", "my_review",)}),)


admin.site.register(IMDbUser, IMDbUserAdmin)
