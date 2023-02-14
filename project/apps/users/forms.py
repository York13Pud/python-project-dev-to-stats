from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from .models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        
        fields = ["username",
                  "password1",
                  "password2",
                  "account_id",  
                  "first_name",
                  "user_summary",
                  "location",
                  "twitter_username", 
                  "github_username",
                  "website_url",
                  "profile_image",
                  "api_key", 
                  "joined_on"]
        
        labels = {"first_name": "Dev.To Name"}
            
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
        
        # --- Settings for read only fields:
        read_only = {"readonly": "readonly",
                     "class": "form-control-plaintext",
                     }
        
        self.fields["account_id"].widget.attrs = read_only
        self.fields["first_name"].widget.attrs = read_only
        self.fields["user_summary"].widget.attrs = read_only
        self.fields["location"].widget.attrs = read_only
        self.fields["twitter_username"].widget.attrs = read_only
        self.fields["github_username"].widget.attrs = read_only
        self.fields["website_url"].widget.attrs = read_only
        self.fields["profile_image"].widget.attrs = read_only
        self.fields["api_key"].widget.attrs = read_only
        self.fields["joined_on"].widget.attrs = read_only


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']