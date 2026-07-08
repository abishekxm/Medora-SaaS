from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField(source='user.get_full_name')

    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('user', 'is_verified', 'created_at', 'updated_at')