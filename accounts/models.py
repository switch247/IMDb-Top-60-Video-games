from django.contrib.auth.models import AbstractUser
from django.db import models
from games.models import VideoGame
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class IMDbUser(AbstractUser):
    nickname = models.CharField(null=True, blank=True, max_length=30)
    user_id = models.CharField(null=True, blank=True, max_length=20)
    bio = models.CharField(null=True, blank=True, max_length=300)
    cover = models.ImageField(upload_to="profile/", default=None, null=True, blank=True)
