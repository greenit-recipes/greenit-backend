import uuid

from django.db import models
from greenit import settings


def get_cover_path(instance, filename):
    if settings.DEBUG:
        return "test/profile/{0}/{1}".format(instance._file_path, filename)
    else:
        return "profile/{0}/{1}".format(instance._file_path, filename)


class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
    liked_recipes = models.ManyToManyField('recipes.Recipe', related_name='liked')
    done_recipes = models.ManyToManyField('recipes.Recipe', related_name='done')
    recipes = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, null=True)
    image = models.FileField(
        max_length=255, upload_to=get_cover_path, null=True, blank=True
    )

    # TO DO: comments =
