# Generated by Django 3.2.9 on 2022-05-17 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fflags', '0001_initial'),
    ]

    operations = [
      migrations.RunSQL("INSERT INTO fflags_fflags(id, name, description, is_active) VALUES(uuid_generate_v4(),'is_out_of_stock','Track stock state',FALSE);"),
      migrations.RunSQL("INSERT INTO fflags_fflags(id, name, description, is_active) VALUES(uuid_generate_v4(), 'is_greenit_full_xp','Track full state',TRUE);"),
    ] 



