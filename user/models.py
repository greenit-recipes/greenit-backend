import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from greenit import settings

from .managers import UserManager


def get_image_path(instance, filename):
    if settings.DEBUG:
        return "test/profile/{0}/{1}".format(instance._file_path, filename)
    else:
        return "profile/{0}/{1}".format(instance._file_path, filename)


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name=_('Email address'), unique=True)
    name = models.CharField(max_length=50, unique=True)
    image_profile = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )
    location = models.CharField(max_length=150)
    auto_pay = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'), default=timezone.now
    )
    dob = models.DateField()
    liked_recipes = models.ManyToManyField('recipe.Recipe', related_name='liked')
    done_recipes = models.ManyToManyField('recipe.Recipe', related_name='done')
    recipes = models.ForeignKey('recipe.Recipe', related_name='authored', on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email

    # TO DO: comments =
