# Generated by Django 3.2.9 on 2022-07-25 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_user_is_recipe_made_beginner_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='particularity_search',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]