# Generated by Django 3.2.9 on 2022-07-26 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ingredient', '0008_migrate_name_url_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientShoppingListUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ingredient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ingredient.ingredient')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientAtHomeUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ingredient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ingredient.ingredient')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
