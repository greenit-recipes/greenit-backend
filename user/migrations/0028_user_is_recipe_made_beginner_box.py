# Generated by Django 3.2.9 on 2022-05-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_user_is_beginner_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_recipe_made_beginner_box',
            field=models.BooleanField(default=False, null=True),
        ),
    ]