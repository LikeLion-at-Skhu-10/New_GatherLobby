from django.db import models

# Create your models here.
class Community(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    def __str__(self):
        return self.text

    blog_id = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='comments',null = True)
    text = models.CharField(max_length=50)
