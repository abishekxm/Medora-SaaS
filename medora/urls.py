"""
URL configuration for medora project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return JsonResponse({
        "status": "success",
        "message": "Medora Backend is Running"
    })

def health_check(request):
    return JsonResponse({"status": "healthy", "service": "medora-django-core"})


urlpatterns = [
    path("", home),

    path("admin/", admin.site.urls),
    path("api/v1/health/", health_check),

    path("api/accounts/", include("accounts.urls")),
    path("api/chatbot/", include("chatbot.urls")),
    path("api/colleges/", include("colleges.urls")),
    path("api/doctor/", include("doctor.urls")),
    path("api/appointments/", include("appointments.urls")),
    path("api/prescriptions/", include("prescriptions.urls")),
    path("api/reviews/", include("reviews.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/videocall/", include("videocall.urls")),
    path("api/study-materials/", include("study_materials.urls")),
    path("api/quiz/", include("quiz.urls")),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
