# Generated by Django 4.1.2 on 2022-10-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_poster_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_poster',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]