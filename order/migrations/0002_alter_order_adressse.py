# Generated by Django 3.2.9 on 2022-05-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='adressse',
            field=models.TextField(max_length=512),
        ),
    ]
