from django.db import models
import uuid

# Create your models here.

class Substance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    group_subs = models.TextField()
    effect = models.TextField()
    
    def __str__(self):
        return self.name