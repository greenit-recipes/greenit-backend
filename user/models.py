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


class UserWantFromGreenit(models.TextChoices):
    DEFAULT_USER_WANT_FROM_GREENIT = 'null', _('null')
    SHARED_TALK = 'shared_talk', _('Shared talk')
    MEET = 'meet', _('Meet')
    FIND_INSPIRATION = 'find_inspiration', _('Find inspiration')


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
        max_length=12,
        default=UserCategoryLvl.DEFAULT_CATEGORY_LVL,
        choices=UserCategoryLvl.choices,
    )
    is_follow_newsletter = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user_want_from_greenit = models.CharField(
        max_length=16,
        default=UserWantFromGreenit.DEFAULT_USER_WANT_FROM_GREENIT,
        choices=UserWantFromGreenit.choices,
    )
    user_category_age = models.CharField(
        max_length=15,
        default=UserCategoryAge.DEFAULT_CATEGORY_AGE,
        choices=UserCategoryAge.choices,
    )
    image_profile = models.FileField(
        max_length=255, upload_to=get_media_path, null=True, blank=True, validators=[file_size_image]
    )
    username = models.CharField(
        max_length=140, unique=True)

    USERNAME_FIELD = "email"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"
    REQUIRED_FIELDS = []
