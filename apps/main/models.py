from django.db import models
from apps.common.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=64)
    subject = models.CharField(max_length=128)
    text = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

