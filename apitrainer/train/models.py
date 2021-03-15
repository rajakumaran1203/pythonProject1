from django.db import models
from uuid import uuid4
# Create your models here.
class Employes(models.Model):
    id = models.UUIDField(default=uuid4,primary_key=True,unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    job = models.CharField(max_length=255)
    address = models.JSONField()
    is_active=models.BooleanField(default=True)
    is_delete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

