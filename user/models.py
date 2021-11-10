import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from greenit import settings

def get_image_path(instance, filename):
    if settings.DEBUG:
        return 'test/profile/{0}/{1}'.format(instance.id, filename)
    else:
        return 'profile/{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        blank=False, max_length=254, verbose_name="email address", unique=True)
    image_profile = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )
    username = models.CharField(
        max_length=140, default='SOME STRING', unique=True)

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"
    REQUIRED_FIELDS = []
