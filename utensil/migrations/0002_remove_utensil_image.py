# Generated by Django 3.2.2 on 2021-11-16 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utensil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utensil',
            name='image',
        ),
    ]