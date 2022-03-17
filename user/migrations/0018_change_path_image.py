from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20220228_1442'),
    ]

    operations = [
      migrations.RunSQL("UPDATE user_user SET image_profile = CONCAT('user/', image_profile) where image_profile != '';"),
    ]
