from django.contrib import admin
from .models import Articles, ArticleComments, ArticleLikes, Followers, Tags


# --- Register your models here.

admin.site.register(Articles)
admin.site.register(ArticleComments)
admin.site.register(ArticleLikes)
admin.site.register(Tags)
admin.site.register(Followers)