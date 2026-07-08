from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.ReadOnlyField(source="patient.username")

    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = (
            "patient",
            "status",
            "created_at",
        )