# Generated by Django 3.2.9 on 2022-02-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20220217_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_facebook',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_google',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
