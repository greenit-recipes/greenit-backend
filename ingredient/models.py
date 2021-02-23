import uuid

from django.db import models
from greenit import settings


def get_image_path(instance, filename):
    if settings.DEBUG:
        return "test/ingredient/{0}/{1}".format(instance._file_path, filename)
    else:
        return "ingredient/{0}/{1}".format(instance._file_path, filename)


class Ingredient(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=256)
    image = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )
    tags = models.ManyToManyField('tag.Tag')

    def __str__(self):
        return self.name