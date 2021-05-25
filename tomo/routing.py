# post/routing.py
from django.urls.conf import path

from . import consumers

websocket_urlpatterns = [
    path('ws/home/', consumers.HomeConsumer.as_asgi()),
]