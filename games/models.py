import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Cast(models.Model):
    pass
class Relation(models.Model):
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

class Rating(models.Model):
    game = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="ratings",
            null=True,
            default=None,
    )
    user = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
            null=True,
            default=None,
    )
    RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]
    your_rating = models.PositiveIntegerField(null=True, blank=True, choices=RATING_CHOICES)
    def __str__(self):
        return str(self.your_rating)

class WatchList(models.Model):
    game = models.ForeignKey(
        VideoGame,
        on_delete=models.CASCADE,
        related_name="watchlists",
        null=True,
        default=None,
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )
    your_watchlist = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.game.title} your - {self.your_watchlist} watchlist"

class Video(models.Model):
    game = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="videos",
            null=True,
            default=None,
    )

    video = models.FileField(upload_to="videos/", null=True, default=None)
    def __str__(self):
        return f"{self.game.title} videos"

class Photo(models.Model):
    game = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="photos",
            null=True,
            default=None,
    )

    photo = models.FileField(upload_to="photos/", null=True, default=None)
    def __str__(self):
        return f"{self.game.title} photos"

class Trivia(models.Model):
    game = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="trivias",
            null=True,
            default=None,
    )
    trivia = models.CharField(max_length=1000, null=True, default=None)
    def __str__(self):
        return self.trivia

class Goof(models.Model):
    game = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="goofs",
            null=True,
            default=None,
    )
    goof = models.CharField(max_length=1000, null=True, default=None)
    def __str__(self):
        return self.goof
class Quote(models.Model):
    game = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="quotes",
            null=True,
            default=None,
    )
    quote = models.CharField(max_length=1000, null=True, default=None)
    def __str__(self):
        return self.quote

class FrequentlyAskedQuestion(models.Model):
    game = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="faqs",
            null=True,
            default=None,
    )
    faq = models.CharField(max_length=1000, null=True, default=None)
    def __str__(self):
        return self.faq

class ParentsGuide(models.Model):
    game = models.ForeignKey(
            VideoGame,
            on_delete=models.CASCADE,
            related_name="parentalguides",
            null=True,
            default=None,
    )
    certification = models.CharField(max_length=1000, null=True, default=None)
    nudity = models.CharField(max_length=1000, null=True, default=None)
    violence = models.CharField(max_length=1000, null=True, default=None)
    profanity = models.CharField(max_length=1000, null=True, default=None)
    drugs = models.CharField(max_length=1000, null=True, default=None)
    intense_scene = models.CharField(max_length=1000, null=True, default=None)
    def __str__(self):
        return self.certification

class Help(models.Model):
    general_information = models.CharField(max_length=1000, null=True, default=None)
    track_games = models.CharField(max_length=1000, null=True, default=None)
    discover = models.CharField(max_length=1000, null=True, default=None)
    featured_content = models.CharField(max_length=1000, null=True, default=None)
    common_issues = models.CharField(max_length=1000, null=True, default=None)
    special_events = models.CharField(max_length=1000, null=True, default=None)
    new_features = models.CharField(max_length=1000, null=True, default=None)
    mobile_web = models.CharField(max_length=1000, null=True, default=None)
    def __str__(self):
        return self.general_information
