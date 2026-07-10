from django.urls import path
from .views import create_admin
from .views import (
    RegisterView,
    ProfileView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("create-admin/", create_admin),
    path("register/", RegisterView.as_view()),
    path("profile/", ProfileView.as_view()),

    # LOGIN
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("password-reset/", PasswordResetRequestView.as_view()),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
    ),
]