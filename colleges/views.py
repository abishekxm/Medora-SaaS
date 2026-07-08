from rest_framework.views import APIView
from rest_framework.response import Response

from .services import (
    predict_colleges,
    get_ai_college_recommendation,
    generate_ai_roadmap,
    get_ai_college_details,
)


class PredictionView(APIView):
    def post(self, request):
        score = int(request.data.get("score"))
        category = request.data.get("category")
        state = request.data.get("state")
        quota = request.data.get("quota")

        colleges = predict_colleges(
            score,
            category,
            state,
            quota,
        )

        ai_recommendation = get_ai_college_recommendation(
            score,
            category,
            state,
            quota,
            colleges,
        )

        selected_college_ai = ""

        if colleges:
            selected_college_ai = get_ai_college_details(colleges[0])

        return Response(
            {
                "colleges": colleges,
                "ai_recommendation": ai_recommendation,
                "selected_college_ai": selected_college_ai,
            }
        )


class RoadmapView(APIView):
    def post(self, request):
        score = request.data.get("score")
        category = request.data.get("category")
        state = request.data.get("state")
        college = request.data.get("college")

        roadmap = generate_ai_roadmap(
            score,
            category,
            state,
            college,
        )

        return Response(
            {
                "roadmap": roadmap,
            }
        )