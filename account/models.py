from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50, null= True, blank= True)
    user_image = models.ImageField(upload_to='images/', blank=True)
