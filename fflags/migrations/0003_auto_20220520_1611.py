# Generated by Django 3.2.9 on 2022-05-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fflags', '0002_seed'),
    ]

    operations = [
        migrations.AddField(
            model_name='fflags',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fflags',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]