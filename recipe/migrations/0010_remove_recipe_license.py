# Generated by Django 3.2 on 2021-06-01 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_recipe_url_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='license',
        ),
    ]
