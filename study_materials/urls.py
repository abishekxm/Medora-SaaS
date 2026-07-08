from django.urls import path
from .views import StudyMaterialView

urlpatterns = [
    path(
        "generate/",
        StudyMaterialView.as_view(),
        name="generate-study-material",
    ),
]