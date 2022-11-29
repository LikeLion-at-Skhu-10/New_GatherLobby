from django.urls import path
from account import views
# static과 media 불러오기 위한 import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name = "signup"),
    path('signin/', views.signin, name = "signin"),
    path('edit_password/',views.edit_password, name='edit_password'),
    path('signin_searchid/', views.signin_searchid, name = "signin_searchid"),
    path('signin_searchpw/', views.signin_searchpw, name = "signin_searchpw"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)