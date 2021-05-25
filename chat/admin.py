from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Message)
admin.site.register(ChatBox)
admin.site.register(GroupChatBox)
admin.site.register(GroupMessage)
admin.site.register(JoinGroupChat)