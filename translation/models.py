import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Translation(models.Model):
    class LanguageChoice(models.TextChoices):
        FRENCH = 'FR', _('French')
        ENGLISH = 'EN', _('English')
        GERMAN = 'DE', _('German')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    language = models.CharField(
        max_length=2, choices=LanguageChoice.choices, default=LanguageChoice.FRENCH
    )
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.language
