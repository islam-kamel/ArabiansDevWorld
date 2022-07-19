from django.urls import path
from feed.views import PostCreateView, PostDetailsView

app_name = "newsfeed"

urlpatterns = [
    path("feed/", PostCreateView.as_view(), name="create_post"),
    path(
        "feed/<str:slug>-<int:pk>",
        PostDetailsView.as_view(),
        name="post_details",
    ),
]
