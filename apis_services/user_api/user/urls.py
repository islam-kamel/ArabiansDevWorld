from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import CreateUserView, UserDetailsView

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
        "user/doc",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("user/register", CreateUserView.as_view(), name="create_user"),
    path("user/<str:username>", UserDetailsView.as_view(), name="user_details"),
    path("user/token/", TokenObtainPairView.as_view(), name="sign_in"),
    path("user/token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
