# Generated by Django 3.2.2 on 2021-11-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0017_recipe_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
