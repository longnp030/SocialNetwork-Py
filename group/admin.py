from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Group)
admin.site.register(GroupAdmin)
admin.site.register(GroupMember)
admin.site.register(GroupPost)
admin.site.register(JoinGroupRequest)
admin.site.register(GroupJoinInvitation)
