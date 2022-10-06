# Generated by Django 3.2.9 on 2022-09-28 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0004_category_ingredient'),
        ('ingredient', '0011_auto_20220928_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='category',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='category_ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_ingredient', to='tag.category_ingredient'),
        ),
    ]