from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0035_auto_20220315_1741'),
    ]

    operations = [
      migrations.RunSQL("UPDATE recipe_recipe SET image = CONCAT('user/', image) where image != '';"),
    ]

