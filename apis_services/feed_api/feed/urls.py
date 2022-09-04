from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from feed.views import PostDetailsView, PostListView
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Feed API",
        default_version="v1",
        description="You can test feed apis",
        terms_of_service="",
        contact=openapi.Contact(email="islam.kamel@agr.svu.edu.eg"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

app_name = "newsfeed"

urlpatterns = [
    path(
        "feed/doc",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("feed/", PostListView.as_view(), name="feed"),
    path(
        "feed/<str:slug>-<int:pk>",
        PostDetailsView.as_view(),
        name="post_details",
    ),
]
