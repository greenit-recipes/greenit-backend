# Generated by Django 3.2.9 on 2022-16-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0007_migrate_data'),
    ]

    operations = [
      migrations.RunSQL("UPDATE ingredient_ingredient SET image = regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(regexp_replace(lower(unaccent(name)), ' ', '_', 'g'), '$', '.jpeg', 'g'), '^', 'ingredient/', 'g'),'\\x27', '_', 'g'), '\\(', '_', 'g'), '\\)', '_', 'g');")
    ]
