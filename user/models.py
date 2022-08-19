import uuid
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from greenit import settings
from utils.file import getFilePathForUpload
from utils.validator import file_size_image


class UserCategoryLvl(models.TextChoices):
    DEFAULT_CATEGORY_LVL = 'null', _('null')
    BEGINNER = 'beginner', _('Beginner')
    INTERMEDIATE = 'intermediate', _('Intermediate')
    ADVANCED = 'advanced', _('Advanced')


class UserCategoryAge(models.TextChoices):
    DEFAULT_CATEGORY_AGE = 'null', _('null')
    YOUNG = 'young', _('Young')
    YOUNG_ADULT = 'young_adult', _('Young adult')
    ADULT = 'adult', _('Adult')
    SENIOR = 'senior', _('Senior')


def get_media_path(instance, filename):
    return getFilePathForUpload(instance.username, "profil", filename)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        blank=False, max_length=254, verbose_name="email address", unique=True)
    user_category_lvl = models.CharField(
        null=True,
        blank=True,
        max_length=12,
        default=UserCategoryLvl.DEFAULT_CATEGORY_LVL,
        choices=UserCategoryLvl.choices,
    )

    is_follow_newsletter = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    ingredient_shopping_list_user = models.ManyToManyField(
        'ingredient.Ingredient',
        through='ingredient.IngredientShoppingListUser',
        related_name='ingredient_ingredientshoppinglistuser',
        blank=True
    )

    ingredient_at_home_user = models.ManyToManyField(
        'ingredient.Ingredient',
        through='ingredient.IngredientAtHomeUser',
        related_name='ingredient_ingredientathomeuser',
        blank=True
    )

    user_category_age = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        default=UserCategoryAge.DEFAULT_CATEGORY_AGE,
        choices=UserCategoryAge.choices,
    )
    image_profile = models.FileField(
        max_length=255, upload_to=get_media_path, null=True, blank=True, validators=[file_size_image]
    )
    username = models.CharField(
        max_length=140, unique=True)
    urls_social_media = models.JSONField(default=dict, null=True, blank=True)
    particularity_search = models.JSONField(default=dict, null=True, blank=True)
    is_creator_profil = models.BooleanField(default=False, null=True)
    is_beginner_box = models.BooleanField(default=False, null=True)
    is_recipe_made_beginner_box = models.BooleanField(default=False, null=True)
    biographie = models.TextField(default='', null=True, blank=True)
    id_facebook = models.CharField(max_length=255, null=True, blank=True)
    id_google = models.CharField(max_length=255, null=True, blank=True)
    photo_url = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = "email"  # e.g: "username", "email"
    EMAIL_FIELD = "email"  # e.g: "email", "primary_email"
    REQUIRED_FIELDS = []
