from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path(route = "", view = views.home_page, name = "home"),
    path(route = "all", view = views.get_users, name = "all_users"),
]


# --- Add URL path for media files (images etc) from settings:
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)