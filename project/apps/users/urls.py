from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path(route = "", view = views.home_page, name = "home"),
    path(route = "login/", view = views.login_user, name = "login"),
    path(route = "logout/", view = views.logout_user, name = "logout"),
    path(route = "register/", view = views.register_user, name = "register"),
    path(route = "account/", view = views.user_account, name = "account"),
]


# --- Add URL path for media files (images etc) from settings:
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)