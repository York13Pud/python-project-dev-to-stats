from django.db import models

import uuid

# --- Create your models here.

class Tags:
    """This is the model for the tags that are used in blog articles."""
    
    id = models.UUIDField(primary_key = True, 
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
        # --- Username is returned from the users table:
        return str(self.name)