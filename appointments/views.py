from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Appointment
from .serializers import AppointmentSerializer
from .services import cancel_appointment, reschedule_appointment


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        appointment = self.get_object()
        cancel_appointment(appointment)
        return Response({
            "status": "appointment cancelled"
        })

    @action(detail=True, methods=["post"])
    def reschedule(self, request, pk=None):
        appointment = self.get_object()

        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")

        reschedule_appointment(
            appointment,
            start_time,
            end_time,
        )

        return Response({
            "status": "appointment rescheduled"
        })
    
    