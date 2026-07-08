from rest_framework.views import APIView
from rest_framework.response import Response

from .services import generate_ai_study_material


class StudyMaterialView(APIView):
    def post(self, request):
        subject = request.data.get("subject")
        topic = request.data.get("topic")
        difficulty = request.data.get("difficulty")

        study_material = generate_ai_study_material(
            subject,
            topic,
            difficulty,
        )

        return Response(
            {
                "study_material": study_material,
            }
        )