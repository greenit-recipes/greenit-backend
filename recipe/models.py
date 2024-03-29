import uuid
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from greenit import settings
from utils.file import getFilePathForUpload
from utils.validator import file_size_image, file_size_video

def get_media_path(instance, filename):
    return getFilePathForUpload(instance.author.username, "recipe", filename)

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
    description = models.TextField(default='')
    title_seo = models.TextField(default='')
    meta_description_seo = models.TextField(default='')
    text_associate = models.TextField(max_length=512, null=True, blank=True)
    video_url = models.TextField(null=True, blank=True)
    video = models.FileField(
        max_length=255, upload_to=get_media_path, null=True, blank=True, validators=[file_size_video]
    )
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
    nbr_view = models.IntegerField(default=0, null=True, blank=True,)
    price_min = models.IntegerField(default=0, null=True, blank=True,)
    price_max = models.IntegerField(default=0, null=True, blank=True,)
    money_saved = models.IntegerField(default=0, null=True, blank=True,)
    plastic_saved = models.IntegerField(default=0, null=True, blank=True,)
    author = models.ForeignKey(
        'user.User',
        related_name='recipe_author',
        on_delete=models.CASCADE,
        null=True,
    )
    image = models.FileField(
        max_length=255, upload_to=get_media_path, null=False, blank=True, validators=[file_size_image], default=''
    )
    tags = models.ManyToManyField('tag.Tag', blank=True)
    substances = models.ManyToManyField('substance.Substance', blank=True)
    category = models.ForeignKey(  # Cheveux/Maison/Bien etre/Corp
        'tag.Category',
        related_name='recipe_category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    likes = models.ManyToManyField(
        'user.User',
        related_name='recipe_like',
        blank=True
    )
    
    favorites = models.ManyToManyField(
        'user.User',
        related_name='recipe_favorite',
        blank=True
    )
    
    ingredients = models.ManyToManyField(
        'ingredient.Ingredient', through='ingredient.IngredientAmount'
    )
    utensils = models.ManyToManyField(
        'utensil.Utensil', through='utensil.UtensilAmount'
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # Instructions is an array of instructions
    # Fields in an instruction:
    # index = position in the instruction list
    # timestamp = timestamp of video where the instructions starts
    # content = the actual instruction
    instructions = models.JSONField(default=dict)
    expiry = models.CharField(max_length=128, default='')
    notes_from_author = models.TextField(default='')
    is_display_home = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.url_id is None:
            self.url_id = slugify(self.name)
        super().save(*args, **kwargs)
     
class Made(models.Model):
    recipe = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE, related_name='recipe_made')
    amount = models.IntegerField()
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='recipe_made_user')    
    created_at = models.DateTimeField(auto_now_add=True, null=True)    
    updated_at = models.DateTimeField(auto_now=True, null=True)