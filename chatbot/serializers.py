from rest_framework import serializers
from .models import ChatSession, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "content", "timestamp")
        read_only_fields = ("id", "timestamp")


class ChatSessionSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatSession
        fields = ("id", "user", "created_at", "messages")
        read_only_fields = ("id", "created_at", "messages")

        