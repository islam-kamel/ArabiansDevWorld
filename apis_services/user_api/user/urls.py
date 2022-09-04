from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView
from user.views import CreateUserView, MyTokenObtainPairView, UserDetailsView

schema_view = get_schema_view(
    openapi.Info(
        title="User API",
        default_version="v1",
        description="You can test feed apis",
        terms_of_service="",
        contact=openapi.Contact(email="islam.kamel@agr.svu.edu.eg"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path(
        "doc", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),
    path("register", CreateUserView.as_view(), name="create_user"),
    path("users/<str:username>", UserDetailsView.as_view(), name="user_details"),
    path("token", MyTokenObtainPairView.as_view(), name="sign_in"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
