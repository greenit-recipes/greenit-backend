# Generated by Django 3.2.9 on 2022-03-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0031_alter_recipe_notes_from_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='money_saved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='plastic_saved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='price_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='price_min',
            field=models.IntegerField(default=0),
        ),
    ]
