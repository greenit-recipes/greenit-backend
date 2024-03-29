# Generated by Django 3.1.7 on 2021-03-10 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0001_initial'),
        ('tag', '0001_initial'),
        ('ingredient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientamount',
            name='recipe',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='recipe.recipe',
            ),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag'),
        ),
    ]
