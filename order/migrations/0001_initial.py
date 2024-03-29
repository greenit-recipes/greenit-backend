# Generated by Django 3.2.9 on 2022-05-04 16:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('adressse', models.TextField(default='')),
                ('postalCode', models.TextField(max_length=50)),
                ('city', models.TextField(max_length=100)),
                ('complementAdresse', models.TextField(max_length=512)),
                ('phone', models.TextField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
