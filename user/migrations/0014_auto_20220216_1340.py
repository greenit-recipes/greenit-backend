# Generated by Django 3.2.9 on 2022-02-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_facebook',
            field=models.IntegerField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='id_google',
            field=models.IntegerField(db_index=True, null=True),
        ),
    ]
