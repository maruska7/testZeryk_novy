# Generated by Django 5.0.3 on 2024-04-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0023_remove_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='recipes'),
        ),
    ]
