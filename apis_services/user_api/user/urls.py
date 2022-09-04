from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from user.views import CreateUserView, MyTokenObtainPairView, UserDetailsView

urlpatterns = [
    path("register", CreateUserView.as_view(), name="create_user"),
    path("users/<str:username>", UserDetailsView.as_view(), name="user_details"),
    path("token", MyTokenObtainPairView.as_view(), name="sign_in"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
