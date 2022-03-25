# Generated by Django 3.2.9 on 2022-03-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0003_alter_tag_ingredient_cuisine'),
        ('substance', '0003_add_subtance_data'),
        ('recipe', '0039_alter_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='substances',
            field=models.ManyToManyField(blank=True, to='substance.Substance'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tag.Tag'),
        ),
    ]
