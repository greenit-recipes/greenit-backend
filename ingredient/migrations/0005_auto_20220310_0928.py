# Generated by Django 3.2.9 on 2022-03-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0004_alter_ingredient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='alternative',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='description',
            field=models.TextField(),
        ),
    ]