from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    content = models.CharField(max_length=140)
    created_by = models.ForeignKey(User)
    created_datetime = models.DateTimeField()