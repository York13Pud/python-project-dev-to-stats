from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["groups", "is_superuser", "user_permissions", "last_login", 
                   "password", "is_staff", "is_active", "last_name",
                   "date_joined"]
        labels = {"first_name": "Dev.To Name"}
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
