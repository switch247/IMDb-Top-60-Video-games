from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import IMDbUser

class IMDbUserCreationForm(UserCreationForm, UserChangeForm):
    class Meta(UserCreationForm):
        model = IMDbUser
        fields = ("nickname", "user_id", "my_rating","bio", "cover", "my_review",) + UserCreationForm.Meta.fields

class IMDbUserChangeForm(UserChangeForm):
    class Meta:
        model = IMDbUser
        fields = ("nickname", "user_id", "my_rating","bio", "cover", "my_review",) + UserCreationForm.Meta.fields
