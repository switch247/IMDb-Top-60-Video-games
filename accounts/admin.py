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
            "username",
            "bio",
            "user_id",
            "cover",
            ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("nickname", "user_id", "bio", "cover" ,)}),)
    addfieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("nickname", "user_id","bio", "cover",)}),)


admin.site.register(IMDbUser, IMDbUserAdmin)
