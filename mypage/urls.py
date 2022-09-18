from django.urls import path, include
from mypage import views
# static과 media 불러오기 위한 import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mypage, name = "mypage"),
    path('mypage_write', views.mypage_write, name = "mypage_write"),
    path('mypage_chat', views.mypage_chat, name = "mypage_chat"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)