# Generated by Django 3.2.2 on 2021-11-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utensil', '0002_remove_utensil_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='utensil',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='utensil',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='utensilamount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='utensilamount',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]