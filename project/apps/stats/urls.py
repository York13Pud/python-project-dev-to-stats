from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path(route = "", view = views.show_stats, name = "stats"),
    path(route = "get-published-articles/", view = views.process_published_articles, name = "get_published_articles"),
    path(route = "get-followers/", view = views.get_follower_count, name = "get_followers"),
    path(route = "testing/", view = views.testing, name = "testing"),
]