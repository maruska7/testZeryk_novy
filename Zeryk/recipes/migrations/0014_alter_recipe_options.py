# Generated by Django 5.0.3 on 2024-04-02 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_comment_body_cz_comment_body_en_ingredient_name_cz_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-created_at']},
        ),
    ]
