# Generated by Django 4.2.4 on 2023-09-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0002_song_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='credit',
            field=models.CharField(default='', max_length=100000),
        ),
    ]
