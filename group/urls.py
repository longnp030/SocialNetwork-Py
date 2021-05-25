from os import name
from tomo import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('create/', create, name='create'),
    path('<int:group_id>/', view, name='view'),
    path('explore/', explore, name='explore'),
    path('<int:group_id>/send_join_request/', send_join_group_request, name='send_join_group_request'),
    path('<int:group_id>/cancel_join_request/', cancel_join_group_request, name='cancel_join_group_request'),
    path('<int:group_id>/<int:user_id>/accept_join_request', accept_join_group_request, name='accept_join_group_request'),
    path('<int:group_id>/<int:user_id>/reject_join_request', reject_join_group_request, name='reject_join_group_request'),
    path('<int:group_id>/leave/', leave_group, name='leave_group'),
    path('<int:group_id>/accept_join_invitation', accept_join_group_invitation, name='accept_join_group_invitation'),
    path('<int:group_id>/reject_join_invitation', reject_join_group_invitation, name='reject_join_group_invitation'),
] + static('images', document_root=settings.POST_IMAGE_DIR)