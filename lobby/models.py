from django.db import models

# Create your models here.
class Lobby(models.Model):
    title = models.CharField(max_length=200)
    area = models.TextField(max_length=20)
    member_number = models.IntegerField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    

    def __str__(self):
        return self.title

class Reply(models.Model):
    def __str__(self):
        return self.text

    lobby_id = models.ForeignKey(Lobby, on_delete=models.CASCADE, related_name='replys',null = True)
    text = models.CharField(max_length=100)

