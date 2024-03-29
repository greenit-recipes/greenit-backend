# Generated by Django 3.1.7 on 2021-03-10 14:31

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'language',
                    models.CharField(
                        choices=[('FR', 'French'), ('EN', 'English'), ('DE', 'German')],
                        default='FR',
                        max_length=2,
                    ),
                ),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
