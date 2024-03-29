# Generated by Django 3.2.9 on 2022-03-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_remove_user_user_want_from_greenit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_category_age',
            field=models.CharField(blank=True, choices=[('null', 'null'), ('young', 'Young'), ('young_adult', 'Young adult'), ('adult', 'Adult'), ('senior', 'Senior')], default='null', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_category_lvl',
            field=models.CharField(blank=True, choices=[('null', 'null'), ('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='null', max_length=12, null=True),
        ),
    ]
