import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from greenit import settings


def get_image_path(instance, filename):
    if settings.DEBUG:
        return "test/recipe/{0}/{1}".format(instance._file_path, filename)
    else:
        return "recipe/{0}/{1}".format(instance._file_path, filename)


class Recipe(models.Model):
    class LanguageChoice(models.TextChoices):
        FRENCH = 'FR', _('French')
        ENGLISH = 'EN', _('English')
        GERMAN = 'DE', _('German')

    class DifficultyChoice(models.TextChoices):
        BEGINNER = 'beginner', _('Beginner')
        INTERMEDIATE = 'intermediate', _('Intermediate')
        ADVANCED = 'advanced', _('Advanced')

    class LicenseChoice(models.TextChoices):
        PLACEHOLDER1 = 'PlaceholderA'
        PLACEHOLDER2 = 'PlaceholderB'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256, default='')
    video_url = models.URLField()
    language = models.CharField(
        max_length=2, choices=LanguageChoice.choices, default=LanguageChoice.FRENCH
    )
    difficulty = models.CharField(
        max_length=12,
        choices=DifficultyChoice.choices,
        default=DifficultyChoice.BEGINNER,
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    duration = models.IntegerField()
    license = models.CharField(
        max_length=12,
        choices=LicenseChoice.choices,
        default=LicenseChoice.PLACEHOLDER1,
    )
    author = models.ForeignKey(
        'user.User',
        related_name='recipe_author',
        on_delete=models.CASCADE,
        null=True,
    )
    image = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )
    tags = models.ManyToManyField('tag.Tag')
    category = models.ForeignKey(
        'tag.Category',
        related_name='recipe_category',
        on_delete=models.CASCADE,
        null=True,
    )
    ingredients = models.ManyToManyField('ingredient.Ingredient')
    instructions = models.TextField(max_length=None, default='')
    utensils = models.ManyToManyField('utensil.Utensil')

    def __str__(self):
        return self.name

    # TO DO: comments =
