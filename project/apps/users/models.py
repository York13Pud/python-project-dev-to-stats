from django.db import models
from django.contrib.auth.models import User


import uuid

# Create your models here.

class Profile(models.Model):
    """_summary_
    This model is used to create a user profile of additional information gathered from dev.to.

    It uses the auth_user table via a one-to-one relationship for the user in the application.
    """
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          unique = True,
                          editable = False)
    
    user = models.OneToOneField(User,
                                on_delete = models.CASCADE,
                                null = True,
                                blank = True)
    
    account_id = models.IntegerField(null = True,
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
                                      default = "profiles/default.png")
    
    joined_on = models.DateTimeField(auto_now_add = False)
    
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """_summary_
            This returns a string representation of the title in the admin panel for a row, rather than the object description.
        Returns:
            This returns a string representation of the title in the admin panel for a row, rather than the object description.
        """
        return str(self.user.username)