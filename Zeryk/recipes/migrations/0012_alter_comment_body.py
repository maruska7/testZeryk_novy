# Generated by Django 5.0.3 on 2024-03-22 18:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_alter_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
