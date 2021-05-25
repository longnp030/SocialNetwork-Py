# chat/routing.py
from django.urls.conf import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/1/', consumers.ChatbotComsumer.as_asgi()),
    path('ws/chat/<slug:user_id>/', consumers.ChatConsumer.as_asgi()),
    path('ws/chat/group/<slug:group_chat_id>/', consumers.GroupChatConsumer.as_asgi()),
]