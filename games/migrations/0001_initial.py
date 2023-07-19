# Generated by Django 4.2.3 on 2023-07-19 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_information', models.CharField(default=None, max_length=1000, null=True)),
                ('track_games', models.CharField(default=None, max_length=1000, null=True)),
                ('discover', models.CharField(default=None, max_length=1000, null=True)),
                ('featured_content', models.CharField(default=None, max_length=1000, null=True)),
                ('common_issues', models.CharField(default=None, max_length=1000, null=True)),
                ('special_events', models.CharField(default=None, max_length=1000, null=True)),
                ('new_features', models.CharField(default=None, max_length=1000, null=True)),
                ('mobile_web', models.CharField(default=None, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('imdb_rating', models.DecimalField(blank=True, decimal_places=2, default=None, editable=False, max_digits=6, null=True)),
                ('cover', models.ImageField(blank=True, default=None, null=True, upload_to='covers/')),
                ('title', models.CharField(default=None, max_length=300, null=True)),
                ('director', models.CharField(default=None, max_length=300, null=True)),
                ('certificate', models.CharField(default=None, max_length=50, null=True)),
                ('writer', models.CharField(default=None, max_length=300, null=True)),
                ('award', models.CharField(default=None, max_length=300, null=True)),
                ('storyline', models.CharField(default=None, max_length=1000, null=True)),
                ('genre', models.CharField(default=None, max_length=300, null=True)),
                ('crazy_credits', models.CharField(default=None, max_length=300, null=True)),
                ('soundtrack', models.CharField(default=None, max_length=300, null=True)),
                ('country_of_origin', models.CharField(default=None, max_length=300, null=True)),
                ('language', models.CharField(default=None, max_length=300, null=True)),
                ('company', models.CharField(default=None, max_length=300, null=True)),
                ('box_office', models.CharField(default=None, max_length=300, null=True)),
                ('color', models.CharField(default=None, max_length=300, null=True)),
                ('soundmix', models.CharField(default=None, max_length=300, null=True)),
                ('nickname', models.CharField(default=None, max_length=300, null=True)),
                ('release_date', models.DateField(default=None, null=True)),
                ('popularity', models.IntegerField(default=None, null=True)),
                ('metascore', models.PositiveIntegerField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(default=None, null=True, upload_to='videos/')),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='games.videogame')),
            ],
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trivia', models.CharField(default=None, max_length=1000, null=True)),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trivias', to='games.videogame')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(default=None, max_length=1000, null=True)),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='games.videogame')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(default=None, null=True, upload_to='photos/')),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='games.videogame')),
            ],
        ),
        migrations.CreateModel(
            name='ParentsGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification', models.CharField(default=None, max_length=1000, null=True)),
                ('nudity', models.CharField(default=None, max_length=1000, null=True)),
                ('violence', models.CharField(default=None, max_length=1000, null=True)),
                ('profanity', models.CharField(default=None, max_length=1000, null=True)),
                ('drugs', models.CharField(default=None, max_length=1000, null=True)),
                ('intense_scene', models.CharField(default=None, max_length=1000, null=True)),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentalguides', to='games.videogame')),
            ],
        ),
        migrations.CreateModel(
            name='Goof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goof', models.CharField(default=None, max_length=1000, null=True)),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goofs', to='games.videogame')),
            ],
        ),
        migrations.CreateModel(
            name='FrequentlyAskedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq', models.CharField(default=None, max_length=1000, null=True)),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='games.videogame')),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('your_watchlist', models.BooleanField(default=False)),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watchlists', to='games.videogame')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('game', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('review', models.CharField(default=None, max_length=1000, null=True)),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='games.videogame')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('game', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('your_rating', models.PositiveIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=None, null=True)),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='games.videogame')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('game', 'user')},
            },
        ),
    ]
