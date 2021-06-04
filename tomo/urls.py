"""tomo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls.conf import include
from django.conf.urls.static import static
from django.urls import path

from .views import *
from tomo import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include(('post.urls', 'post'), namespace='post')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('chat/', include(('chat.urls', 'chat'), namespace='chat')),
    path('group/', include(('group.urls', 'group'), namespace='group')),
    path('search/<str:filename>/', search, name='search'),
    path('', home, name='home'),
] + static('images', document_root=settings.POST_IMAGE_DIR)
