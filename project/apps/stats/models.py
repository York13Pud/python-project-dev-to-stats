from django.db import models
from users.models import User

import uuid

# --- Create your models here.

class Tags(models.Model):
    """This is the model for the tags that are used in blog articles."""
    
    tag_id = models.UUIDField(primary_key = True, 
                              default = uuid.uuid4, 
                              unique = True, 
                              editable = False)
    name = models.TextField(max_length = 50, 
                            null = False, 
                            blank = False)
    date_added = models.DateTimeField(auto_now_add = True, 
                                      null = False, 
                                      blank = False)

    def __str__(self):
        """_summary_
            This returns a string representation of the name in the admin panel for a row, rather than the object description.
        Returns:
            This returns a string representation of the name in the admin panel for a row, rather than the object description.
        """
        
        # --- Name is returned from the tags table:
        return str(self.name)
    

class Articles(models.Model):
    """This is the model for storing the articles that are collected from the blog site"""
    
    article_id = models.UUIDField(primary_key = True, 
                              default = uuid.uuid4, 
                              unique = True, 
                              editable = False)
    article_user_id_fk = models.ForeignKey(to = User, 
                                           null = True, 
                                           blank = True, 
                                           on_delete = models.SET_NULL)
    reference_id = models.TextField(max_length = 50, 
                                    null = False, 
                                    blank = False)
    title = models.TextField(max_length = 200,
                             null = False, 
                             blank = False)
    is_published = models.BooleanField()
    published_date = models.DateTimeField(auto_now_add = False,
                                          null = True, 
                                          blank = True)    
    url = models.URLField(max_length = 1000, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True, 
                                      null = False, 
                                      blank = False)
    tags = models.ManyToManyField(to = Tags,
                                  blank = True, 
                                  null=True)
    
    def __str__(self):
        """_summary_
            This returns a string representation of the name in the admin panel for a row, rather than the object description.
        Returns:
            This returns a string representation of the name in the admin panel for a row, rather than the object description.
        """
        
        # --- title is returned from the articles table:
        return str(self.title)