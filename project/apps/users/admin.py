from django.contrib import admin
from .models import User


# --- Register your models here that need to show in the admin portal:
admin.site.register(User)