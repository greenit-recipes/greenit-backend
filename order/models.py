# Create your models here.
import uuid

from django.db import models


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.TextField(max_length=50)
    adressse = models.TextField(max_length=512)
    postalCode = models.TextField(max_length=50)
    city = models.TextField(max_length=100)
    complementAdresse = models.TextField(max_length=512)
    phone = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name