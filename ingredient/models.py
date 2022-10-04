import uuid

from django.db import models

from greenit import settings
from utils.file import getFilePathForUpload
from django.utils.text import slugify


def get_image_path(instance, filename):
    return getFilePathForUpload("", "ingredient", filename)


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=45)
    description = models.TextField()
    alternative = models.TextField(null=True)
    information_market = models.TextField(null=True, blank=True)
    indication = models.TextField(null=True, blank=True)
    precaution = models.TextField(null=True, blank=True)
    contenance = models.TextField(null=True, blank=True)
    rating = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    producer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_for_market = models.BooleanField(default=False)
    is_supermarket = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    is_productor = models.BooleanField(default=False)
    image = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )
    image_optional2 = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )
    image_optional3 = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )
    tags = models.ManyToManyField('tag.Tag')
    category_ingredient = models.ForeignKey(  # Poudres et argiles/Huiles végétales et macérâts/Huiles essentielles/
        'tag.Category_Ingredient',
        related_name='category_ingredient',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.CharField(max_length=16)
    ingredient = models.ForeignKey(
        'ingredient.Ingredient',
        on_delete=models.CASCADE,
        null=True,
    )
    recipe = models.ForeignKey(
        'recipe.Recipe',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f'{self.amount} {self.ingredient}'


class IngredientShoppingListUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ingredient = models.ForeignKey(
        'ingredient.Ingredient',
        on_delete=models.CASCADE,
        null=True,
    )
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f'{self.ingredient}'


class IngredientAtHomeUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ingredient = models.ForeignKey(
        'ingredient.Ingredient',
        on_delete=models.CASCADE,
        null=True,
    )

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f'{self.ingredient}'
