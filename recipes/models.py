import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from greenit import settings


def get_cover_path(instance, filename):
    if settings.DEBUG:
        return "test/recipe/{0}/{1}".format(instance._file_path, filename)
    else:
        return "recipe/{0}/{1}".format(instance._file_path, filename)


class Recipe(models.Model):
    class LanguageChoices(models.TextChoices):
        FRENCH = 'FR', _('French')
        ENGLISH = 'EN', _('English')
        GERMAN = 'DE', _('German')

    class DifficultyChoices(models.TextChoices):
        BEGINNER = 'beginner', _('Beginner')
        INTERMEDIATE = 'intermediate', _('Intermediate')
        ADVANCED = 'advanced', _('Advanced')

    class LicenseChoices(models.TextChoices):
        PLACEHOLDER1 = 'PlaceholderA'
        PLACEHOLDER2 = 'PlaceholderB'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    video_url = models.URLField()
    language = models.CharField(
        max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.FRENCH
    )
    license = models.CharField(
        max_length=12,
        choices=LicenseChoices.choices,
        default=LicenseChoices.PLACEHOLDER1,
    )
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)

    image = models.FileField(
        max_length=255, upload_to=get_cover_path, null=True, blank=True
    )
    tags = models.ManyToManyField('tags.Tag')
    ingredients = models.ManyToManyField('ingredients.Ingredient')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    utensils = models.ManyToManyField('utensils.Utensil')
    difficulty = models.CharField(
        max_length=12,
        choices=DifficultyChoices.choices,
        default=DifficultyChoices.BEGINNER,
    )
    duration = models.IntegerField()

    # TO DO: comments =
