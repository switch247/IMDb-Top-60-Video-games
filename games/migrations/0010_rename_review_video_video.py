# Generated by Django 4.2.3 on 2023-07-16 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='review',
            new_name='video',
        ),
    ]
