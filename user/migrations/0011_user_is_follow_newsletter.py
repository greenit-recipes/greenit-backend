# Generated by Django 3.2.2 on 2021-12-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_user_image_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_follow_newsletter',
            field=models.BooleanField(default=False),
        ),
    ]
