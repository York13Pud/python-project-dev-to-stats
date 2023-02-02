from django.db import models
from django.contrib.auth.models import User


import uuid

# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4)
    user = models.OneToOneField(to = User,
                                on_delete = models.CASCADE,
                                null = True,
                                blank = True)
    