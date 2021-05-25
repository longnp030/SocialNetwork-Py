from os import name
from django.urls import path

from .views import *

urlpatterns = [
    path('', messenger, name='messenger'),
    path('<int:user_id>/', room, name='room'),
    path('<int:creator_id>/create_group_chat', create_group_chat, name='create_group_chat'),
    path('group/<slug:group_chat_id>/', group_room, name='group_room'),
    path('group/<slug:group_chat_id>/<int:member_id>/kick/', kick, name='kick'),
    path('group/<slug:group_chat_id>/leave/', leave, name='leave'),
]