from django.urls import path
from .views import ChatSessionListCreateView, MessageCreateView

urlpatterns = [
    path('sessions/', ChatSessionListCreateView.as_view(), name='chat-sessions'),
    path('sessions/<int:session_id>/messages/', MessageCreateView.as_view(), name='chat-messages'),
]
