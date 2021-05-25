from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from .views import *
from tomo import settings

urlpatterns = [
    path(r'register/', CreateUserView.as_view()),
    path(r'login/', LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    path(r'logout/', LogoutView.as_view(), {'next_page': '/'}),
    path(r'<int:user_id>/', user_profile, name='user_profile'),
    path(r'<int:user_id>/send_fr_req', send_friend_request, name='send_friend_request'),
    path(r'<int:user_id>/cancel_fr_req', cancel_friend_request, name='cancel_friend_request'),
    path(r'<int:user_id>/accept_fr_req', accept_friend_request, name='accept_friend_request'),
    path(r'<int:user_id>/reject_fr_req', reject_friend_request, name='reject_friend_request'),
    path(r'<int:user_id>/unfriend', unfriend, name='unfriend'),
] + static('images', document_root=settings.USER_IMAGE_DIR)