# Generated by Django 3.2.9 on 2022-10-04 10:52

from django.db import migrations, models
import ingredient.models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0018_ingredient_image_optional2'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='image_optional3',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=ingredient.models.get_image_path),
        ),
    ]
