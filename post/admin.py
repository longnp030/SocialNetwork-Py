from post.models import *
from django.contrib import admin

# Register your models here.

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(PostImage)
admin.site.register(Reaction)
admin.site.register(Comment)