from django.db import models
import uuid


class FFlags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=45)
    description = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
