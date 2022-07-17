from django.urls import path
from user.views import CreateUserView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

url_path = "users/<str:username>"
api_version = "v1"

urlpatterns = [
    path("users", CreateUserView.as_view(), name="user_details"),
    path("token", TokenObtainPairView.as_view(), name="signin"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
]
