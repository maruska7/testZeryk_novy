# Generated by Django 5.0.3 on 2024-03-13 23:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(related_name='recipe_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
