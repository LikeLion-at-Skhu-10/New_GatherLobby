from django.urls import path, include
from lobby import views
# static과 media 불러오기 위한 import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.lobby , name = "lobby"),
    path('lobby_write/', views.lobby_write, name = "lobby_write"),
    path('lobby_read/', views.lobby_read, name = "lobby_read"),
    path('lobby_detail/', views.lobby_detail, name = "lobby_detail"),
    path('lobby_edit/', views.lobby_edit, name = "lobby_edit"),
    path('lobby_chat/', views.lobby_chat, name = "lobby_chat"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)