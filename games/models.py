import uuid
from django.db import models
from django.urls import reverse


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
class Review(models.Model):
    pass
class FrequentlyAskedQuestion(models.Model):
    pass

class VideoGame(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    cover = models.ImageField(upload_to="covers/", default=None, null=True, blank=True)
    title = models.CharField(max_length=40, default=None, null=True)
    director = models.ForeignKey(
            Director,
            on_delete=models.CASCADE,
            related_name="directors",
            null=True,
            default=None,
    )
    writer = models.ForeignKey(
            Writer,
            on_delete=models.CASCADE,
            related_name="writers",
            null=True,
            default=None,

    )
    cast = models.ForeignKey(
            Cast,
            on_delete=models.CASCADE,
            related_name="casts",
            null=True,
            default=None,

    )
    award = models.CharField(max_length=40, default=None, null=True)
    video = models.FileField(upload_to="videos/", default=None, null=True, blank=True)
    photo = models.ImageField(upload_to="photos/", default=None, null=True, blank=True)
    relation = models.ForeignKey(
            Relation,
            on_delete=models.CASCADE,
            related_name="relations",
            null=True,
            default=None,

    )
    storyline = models.CharField(max_length=200, default=None, null=True)
    genre = models.CharField(max_length=20, default=None, null=True)
    trivia = models.ForeignKey(
            Trivia,
            on_delete=models.CASCADE,
            related_name="Trivias",
            null=True,
            default=None,
    )
    goof = models.ForeignKey(
            Goof,
            on_delete=models.CASCADE,
            related_name="goofs",
            null=True,
            default=None,

    )
    quote = models.ForeignKey(
            Quote,
            on_delete=models.CASCADE,
            related_name="quotes",
            null=True,
            default=None,

    )
    crazy_credits = models.CharField(max_length=40, default=None, null=True)
    soundtrack = models.CharField(max_length=20, default=None, null=True)
    review = models.ForeignKey(
            Review,
            on_delete=models.CASCADE,
            related_name="reviews",
            null=True,
            default=None,

    )
    picks = models.ForeignKey(
            'self',
            on_delete=models.CASCADE,
            null=True,
            default=None,
    )
    country_of_origin = models.CharField(max_length=20, default=None, null=True)
    language = models.CharField(max_length=20, default=None, null=True)
    company = models.CharField(max_length=20, default=None, null=True)
    box_office = models.CharField(max_length=20, default=None, null=True)
    runtime = models.TimeField(auto_now=False, default=None, null=True)
    frequent_questions = models.ForeignKey(
            FrequentlyAskedQuestion,
            on_delete=models.CASCADE,
            related_name="FAQs",            
            null=True,
            default=None,

    )
    color = models.CharField(max_length=10, default=None, null=True)
    soundmix = models.CharField(max_length=10, default=None, null=True)
    nickname = models.CharField(max_length=20, default=None, null=True)
    parents_guide = models.ForeignKey(
            ParentsGuide,
            on_delete=models.CASCADE,
            related_name="parental_guides",
            null=True,
            default=None,
    )
    release_date = models.DateField(default=None, null=True)
    imdb_rating = models.DecimalField(max_digits=6, decimal_places=2, default=None, null=True)
    popularity = models.IntegerField(default=None, null=True)
    metascore = models.PositiveIntegerField(default=None, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("game_detail", args =[str(self.id)])
