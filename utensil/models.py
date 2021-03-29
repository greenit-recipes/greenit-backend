import uuid

from django.db import models

from greenit import settings


def get_image_path(instance, filename):
    if settings.DEBUG:
        return "test/utensil/{0}/{1}".format(instance.id, filename)
    else:
        return "utensil/{0}/{1}".format(instance.id, filename)


class Utensil(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=256)
    image = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )
    tags = models.ManyToManyField('tag.Tag')

    def __str__(self):
        return self.name


class UtensilAmount(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.CharField(max_length=16)
    utensil = models.ForeignKey(
        'utensil.Utensil',
        on_delete=models.CASCADE,
        null=True,
    )
    recipe = models.ForeignKey(
        'recipe.Recipe',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f'{self.amount} {self.utensil}'
