from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_user_is_follow_newsletter'),
    ]

    operations = [
      migrations.RunSQL("DELETE FROM user_user WHERE id='e122f0bf-e67d-40cf-ba78-d00f881d7cbf'"),
      migrations.RunSQL("INSERT INTO graphql_auth_userstatus(verified, archived, user_id) VALUES(TRUE, FALSE, '38b3dc6d-a3f5-4f65-85ea-a765d140584f') RETURNING id, verified, archived, secondary_email, user_id;"),
    ]
