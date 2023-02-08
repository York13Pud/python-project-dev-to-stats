from django.db import models
from django.contrib.auth.models import AbstractUser
from django_cryptography.fields import encrypt


# --- Create the user application models here:
class User(AbstractUser):
    """This class will Abstract the built-in django Users model and expand it with the below fields.
    The login method (username and password) will not change"""
    
    account_id = models.IntegerField(null = True, blank = True)
    user_summary = models.TextField(max_length = 2000, null = True, blank = True)
    location = models.CharField(max_length = 500, null = True, blank = True)
    twitter_username = models.CharField(max_length = 100, null = True, blank = True)
    github_username = models.CharField(max_length = 100, null = True, blank = True)
    website_url = models.URLField(max_length = 250, null = True, blank = True)
    # --- Note: Change profile_image to URLField
    profile_image = models.ImageField(null = True,  blank = True, upload_to = "profiles/",
                                      default = "profiles/default.png")
    api_key = encrypt(models.CharField(max_length = 50, null = True, blank = True))
    joined_on = models.DateTimeField(auto_now_add = False, null = True, blank = True)

    def __str__(self):
        """_summary_
            This returns a string representation of the username in the admin panel for a row, rather than the object description.
        Returns:
            This returns a string representation of the username in the admin panel for a row, rather than the object description.
        """
        # --- Username is returned from the users table:
        return str(self.username)
