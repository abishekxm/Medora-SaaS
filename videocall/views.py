from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from appointments.models import Appointment
from .models import VideoRoom
from .serializers import VideoRoomSerializer
from rest_framework.permissions import IsAuthenticated


class CreateVideoRoom(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, appointment_id):

        appointment = get_object_or_404(
            Appointment,
            id=appointment_id
        )

        room_name = f"room-{appointment.id}"
        meeting_link = f"https://meet.jit.si/{room_name}"

        room, created = VideoRoom.objects.get_or_create(
            room_name=room_name,
            defaults={
                "doctor": appointment.doctor.user,
                "patient": appointment.patient,
                "meeting_link": meeting_link,
            },
        )

        serializer = VideoRoomSerializer(room)
        return Response(serializer.data)


class VideoRoomDetail(generics.RetrieveAPIView):
    queryset = VideoRoom.objects.all()
    serializer_class = VideoRoomSerializer
    permission_classes = [permissions.AllowAny]


class DoctorRooms(generics.ListAPIView):
    serializer_class = VideoRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return VideoRoom.objects.filter(
            doctor=self.request.user
        ).order_by("-created_at")


class PatientRooms(generics.ListAPIView):
    serializer_class = VideoRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return VideoRoom.objects.filter(
            patient=self.request.user
        ).order_by("-created_at")


class EndConsultation(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, pk):

        room = get_object_or_404(VideoRoom, pk=pk)

        room.is_active = False
        room.save()

        return Response({
            "message": "Consultation ended successfully."
        })
    
    