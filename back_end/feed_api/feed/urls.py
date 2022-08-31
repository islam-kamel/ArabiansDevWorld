from django.urls import path
from feed.views import PostDetailsView, PostListView

app_name = "newsfeed"

urlpatterns = [
    path("feed/", PostListView.as_view(), name="feed"),
    path(
        "feed/<str:slug>-<int:pk>",
        PostDetailsView.as_view(),
        name="post_details",
    ),
]
