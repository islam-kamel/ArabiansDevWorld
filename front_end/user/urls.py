from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("signin", views.login_user, name="login"),
    path("signup", views.register, name="register"),
    path("logout", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("profile_update/", views.profile_update, name="profile_update"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
