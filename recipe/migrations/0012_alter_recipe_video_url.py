# Generated by Django 3.2 on 2021-06-05 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0011_merge_20210601_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='video_url',
            field=models.CharField(max_length=255),
        ),
    ]
