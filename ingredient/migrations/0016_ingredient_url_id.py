# Generated by Django 3.2.9 on 2022-09-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0015_remove_ingredient_url_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='url_id',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
