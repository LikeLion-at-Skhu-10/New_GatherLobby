from django.urls import path
from community import views
# static과 media 불러오기 위한 import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.community , name = "community"),
    path('community_write/', views.community_write, name = "community_write"),
    path('community_read/', views.community_read, name = "community_read"),
    path('community_detail/', views.community_detail, name = "community_detail"),
    path('community_edit/', views.community_edit, name = "community_edit"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)