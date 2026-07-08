from rest_framework import serializers
from .models import VideoRoom


class VideoRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoRoom
        fields = "__all__"

        