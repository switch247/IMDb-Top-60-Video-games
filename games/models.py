import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Director(models.Model):
    pass

class Writer(models.Model):
    pass

class Cast(models.Model):
    pass

class Relation(models.Model):
    pass
class Trivia(models.Model):
    pass
class ParentsGuide(models.Model):
    pass
class Goof(models.Model):
    pass
class Quote(models.Model):
    pass

class FrequentlyAskedQuestion(models.Model):
    pass

class VideoGame(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    cover = models.ImageField(upload_to="covers/", default=None, null=True, blank=True)
    title = models.CharField(max_length=300, default=None, null=True)
    director = models.CharField(max_length=300, default=None, null=True)
    certificate = models.CharField(max_length=50, default=None, null=True)
    writer = models.CharField(max_length=300, default=None, null=True)
    award = models.CharField(max_length=300, default=None, null=True)
    storyline = models.CharField(max_length=1000, default=None, null=True)
    genre = models.CharField(max_length=300, default=None, null=True)
    crazy_credits = models.CharField(max_length=300, default=None, null=True)
    soundtrack = models.CharField(max_length=300, default=None, null=True)
    country_of_origin = models.CharField(max_length=300, default=None, null=True)
    language = models.CharField(max_length=300, default=None, null=True)
    company = models.CharField(max_length=300, default=None, null=True)
    box_office = models.CharField(max_length=300, default=None, null=True)
    runtime = models.TimeField(auto_now=False, default=None, null=True)
    color = models.CharField(max_length=300, default=None, null=True)
    soundmix = models.CharField(max_length=300, default=None, null=True)
    nickname = models.CharField(max_length=300, default=None, null=True)
    release_date = models.DateField(default=None, null=True)
    imdb_rating = models.DecimalField(max_digits=6, decimal_places=2, default=None, null=True)
    popularity = models.IntegerField(default=None, null=True)
    metascore = models.PositiveIntegerField(default=None, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("game_detail", args =[str(self.id)])

class Review(models.Model):
    game = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="reviews",
            null=True,
            default=None,
    )
    user = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
            null=True,
            default=None,
    )
    review = models.CharField(max_length=1000, null=True, default=None)
    def __str__(self):
        return self.review
class Video:
    pass
class Photo:
    pass
