from django.db import models
from django.contrib.auth.models import User


import uuid

# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          unique = True,
                          editable = False)
    user = models.OneToOneField(to = User,
                                on_delete = models.CASCADE,
                                null = True,
                                blank = True)
    account_id = models.IntegerField(max_length = 10,
                                     null = True,
                                     blank = True)
    user_summary = models.CharField(max_length = 2000,
                                    null = True,
                                    blank = True)
    location = models.CharField(max_length = 500,
                                null = True,
                                blank = True)
    twitter_username = models.CharField(max_length = 100,
                                        null = True,
                                        blank = True)
    github_username = models.CharField(max_length = 100,
                                       null = True,
                                       blank = True)
    website_url = models.URLField(max_length = 250,
                                  null = True,
                                  blank = True)
    profile_image = models.ImageField(null = True, 
                                      blank = True,
                                      upload_to = "profiles/",
                                      default = "profiles/user-default.png")
    joined_on = models.DateTimeField(auto_now_add = False)
    date_added = models.DateTimeField(auto_now_add = True)