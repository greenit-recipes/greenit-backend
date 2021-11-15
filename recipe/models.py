import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from greenit import settings


def get_image_path(instance, filename):
    if settings.DEBUG:
        return 'test/recipe/{0}/{1}'.format(instance.id, filename)
    else:
        return 'recipe/{0}/{1}'.format(instance.id, filename)


class Recipe(models.Model):
    class LanguageChoice(models.TextChoices):
        FRENCH = 'FR', _('French')
        ENGLISH = 'EN', _('English')
        GERMAN = 'DE', _('German')

    class DifficultyChoice(models.TextChoices):
        BEGINNER = 'beginner', _('Beginner')
        INTERMEDIATE = 'intermediate', _('Intermediate')
        ADVANCED = 'advanced', _('Advanced')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url_id = models.SlugField(unique=True, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=512, default='')
    text_associate = models.TextField(max_length=512, null=True, blank=True)
    video_url = models.CharField(max_length=255)
    language = models.CharField(
        max_length=2, choices=LanguageChoice.choices, default=LanguageChoice.FRENCH
    )
    difficulty = models.CharField(
        max_length=12,
        choices=DifficultyChoice.choices,
        default=DifficultyChoice.BEGINNER,
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True
    )
    duration = models.IntegerField()
    author = models.ForeignKey(
        'user.User',
        related_name='recipe_author',
        on_delete=models.SET_NULL,
        null=True,
    )
    image = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )
    tags = models.ManyToManyField('tag.Tag')
    category = models.ForeignKey(
        'tag.Category',
        related_name='recipe_category',
        on_delete=models.SET_NULL,
        null=True,
    )
    ingredients = models.ManyToManyField(
        'ingredient.Ingredient', through='ingredient.IngredientAmount'
    )
    utensils = models.ManyToManyField(
        'utensil.Utensil', through='utensil.UtensilAmount'
    )
    # Instructions is an array of instructions
    # Fields in an instruction:
    # index = position in the instruction list
    # timestamp = timestamp of video where the instructions starts
    # content = the actual instruction
    instructions = models.JSONField(default=dict)
    expiry = models.CharField(max_length=128, default='')
    notes_from_author = models.CharField(max_length=256, default='')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.url_id is None:
            self.url_id = slugify(self.name)
        super().save(*args, **kwargs)
