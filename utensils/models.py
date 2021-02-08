import uuid

from django.db import models
from greenit import settings


def get_cover_path(instance, filename):
    if settings.DEBUG:
        return "test/utensils/{0}/{1}".format(instance._file_path, filename)
    else:
        return "utensils/{0}/{1}".format(instance._file_path, filename)


class Utensil(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=256)
    image = models.FileField(
        max_length=255, upload_to=get_cover_path, null=True, blank=True
    )
    tags = models.ManyToManyField('tags.Tag')
