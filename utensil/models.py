import uuid

from django.db import models

from greenit import settings
from utils.file import getFilePathForUpload


def get_image_path(instance, filename):
    return getFilePathForUpload("", "utensil", filename)


class Utensil(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=256)
    tags = models.ManyToManyField('tag.Tag')
    image = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.name


class UtensilAmount(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
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
