from django.urls import path
from user.views import CreateUserView, UpdateUserInfo
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

url_path = "users/<str:username>"
api_version = "v1"

urlpatterns = [
    path("users", CreateUserView.as_view(), name="user_details"),
    path(
        "users/<str:username>",
        UpdateUserInfo.as_view(),
        name="update_user_info",
    ),
    path("token", TokenObtainPairView.as_view(), name="signin"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
]
