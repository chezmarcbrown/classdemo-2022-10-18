# Generated by Django 4.1.2 on 2022-10-20 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookers', to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.passenger')),
            ],
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='flights',
        ),
        migrations.AddField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', through='flights.Booking', to='flights.flight'),
        ),

    ]
