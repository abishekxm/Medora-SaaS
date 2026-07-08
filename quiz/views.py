from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Quiz
from .serializers import QuizSerializer
from .services import generate_ai_quiz
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView


class GenerateQuizView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        topic = request.data.get("topic")

        if not topic:
            return Response(
                {"error": "Topic is required"},
                status=400,
            )

        questions = generate_ai_quiz(topic)

        quiz = Quiz.objects.create(
            user=request.user,
            topic=topic,
            total_questions=len(questions),
            score=0,
        )

        return Response(
            {
                "quiz": QuizSerializer(quiz).data,
                "questions": questions,
            }
        )
    
class SubmitQuizView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, quiz_id):
        quiz = get_object_or_404(
            Quiz,
            id=quiz_id,
            user=request.user,
        )

        score = request.data.get("score", 0)

        quiz.score = score
        quiz.save()

        return Response(
            {
                "message": "Quiz submitted successfully",
                "score": quiz.score,
            }
        )
class QuizHistoryView(ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Quiz.objects.filter(
            user=self.request.user
        ).order_by("-created_at")
    
