# Generated by Django 4.1.2 on 2022-10-20 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_movie_poster_url_alter_movie_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]