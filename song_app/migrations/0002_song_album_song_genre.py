# Generated by Django 5.0.6 on 2024-06-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
