from django.urls import path
from .views import GenerateQuizView, SubmitQuizView
from .views import (
    GenerateQuizView,
    SubmitQuizView,
    QuizHistoryView,
)

urlpatterns = [
    path(
        "generate/",
        GenerateQuizView.as_view(),
        name="generate-quiz",
    ),
    path(
        "submit/<int:quiz_id>/",
        SubmitQuizView.as_view(),
        name="submit-quiz",
    ),
    path(
    "history/",
    QuizHistoryView.as_view(),
    name="quiz-history",
),
]