from django.contrib import admin
from .models import Profile


# --- Register your models here that need to show in the admin portal:
admin.site.register(Profile)