# Generated by Django 3.2.9 on 2022-03-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0005_auto_20220310_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='is_productor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='is_supermarket',
            field=models.BooleanField(default=False),
        ),
    ]