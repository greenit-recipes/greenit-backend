# Generated by Django 3.2.9 on 2022-03-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substance', '0001_initial'),
        ('recipe', '0032_auto_20220315_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='substances',
            field=models.ManyToManyField(to='substance.Substance'),
        ),
    ]
