from django.contrib.auth.models import AbstractUser
from django.db import models
from games.models import VideoGame
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class IMDbUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=30)
    user_id = models.CharField(null=True, blank=True, max_length=20)
    my_rating = models.PositiveIntegerField(null=True, blank=True, validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
            ]
    )
    bio = models.CharField(null=True, blank=True, max_length=300)
    cover = models.ImageField(upload_to="profile/", default=None, null=True, blank=True)
    my_review = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="reviews",
            null=True,
            default=None,
    )
    my_watchlist = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="watchlists",
            null="True",
            default=None,
    )
