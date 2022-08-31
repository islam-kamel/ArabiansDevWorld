from django.urls import path, re_path

from . import views
from .views import PostCreateView, PostDeleteView, PostUpdateView

regx = "([aA-zZ0-9أ-ىا-ي]+(-))*(\d)*"
urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("feed/", views.home, name="home"),
    path("new_post", PostCreateView.as_view(), name="new_post"),
    re_path(
        f"detail/(?P<slug>{regx})/$", views.PostDetailsView.as_view(), name="detail"
    ),
    re_path(
        f"detail/update/(?P<slug>{regx})/$",
        PostUpdateView.as_view(),
        name="post-update",
    ),
    re_path(
        f"detail/delete/(?P<slug>{regx})/$",
        PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("about/", views.about, name="about"),
]
