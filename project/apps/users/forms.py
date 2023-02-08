from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        
        fields = ["account_id", 
                  "username", 
                  "first_name",
                  "user_summary",
                  "location",
                  "twitter_username", 
                  "github_username",
                  "website_url",
                  "profile_image",
                  "api_key", 
                  "joined_on",
                  "password1"]
        
        labels = {"first_name": "Dev.To Name"}
            
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
