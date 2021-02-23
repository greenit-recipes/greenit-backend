# Generated by Django 3.1.6 on 2021-02-22 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20210218_1526'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='recipe',
        ),
        migrations.AddField(
            model_name='user',
            name='recipes',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='authored',
                to='recipe.recipe',
            ),
        ),
    ]
