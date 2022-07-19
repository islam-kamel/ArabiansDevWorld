from django.urls import path

from . import views
from .views import PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("feed/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("detail/<str:slug>", views.post_detail, name="detail"),
    path("new_post", PostCreateView.as_view(), name="new_post"),
    path(
        "detail/<slug:pk>/update/",
        PostUpdateView.as_view(),
        name="post-update",
    ),
    path(
        "detail/<str:slug>-<int:pk>/delete/",
        PostDeleteView.as_view(),
        name="post-delete",
    ),
]
