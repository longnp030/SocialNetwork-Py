from django.conf.urls.static import static
from django.urls import path

from .views import *
from tomo import settings

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('<int:group_id>/create/', create_post, name='create_post'),
    path('create/<int:post_id>/add_images', add_img, name='add_img'),
    path('<int:post_id>/', post_view, name='post_view'),
    path('<int:post_id/edit/', edit, name='edit'),
    path('<int:post_id>/like/', like_post, name='like'),
    path('<int:post_id>/unlike/', unlike_post, name='unlike'),
    path('<int:post_id>/delete/', delete, name='delete'),
    path('<int:post_id>/edit/', edit, name='edit'),
] + static('images', document_root=settings.POST_IMAGE_DIR)