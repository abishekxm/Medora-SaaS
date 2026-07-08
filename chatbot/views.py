from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import ChatSession, Message
from .serializers import ChatSessionSerializer, MessageSerializer
from .services import get_ai_response


class ChatSessionListCreateView(generics.ListCreateAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # If ChatSession.user allows null
        serializer.save(user=None)

        # If user is REQUIRED instead, replace the above line with:
        # serializer.save(user_id=1)


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        session = ChatSession.objects.get(pk=self.kwargs["session_id"])

        # Save user message
        user_message = serializer.save(
            session=session,
            sender="user"
        )

        # Generate AI response
        ai_response = get_ai_response(user_message.content)

        # Save bot response
        Message.objects.create(
            session=session,
            sender="bot",
            content=ai_response
        )

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        session = ChatSession.objects.get(pk=self.kwargs["session_id"])
        bot_message = session.messages.filter(sender="bot").last()

        return Response({
            "user_message": response.data,
            "bot_response": bot_message.content if bot_message else ""
        })
