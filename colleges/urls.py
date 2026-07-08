from django.urls import path
from .views import PredictionView, RoadmapView

urlpatterns = [
    path(
        "predict/",
        PredictionView.as_view(),
        name="college-predict",
    ),

    path(
        "roadmap/",
        RoadmapView.as_view(),
        name="ai-roadmap",
    ),
]
