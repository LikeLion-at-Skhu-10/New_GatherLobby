from django.db import models

# Create your models here.
class Lobby(models.Model):
    title = models.CharField(max_length=200)
    area = models.TextField(max_length=20)
    member_number = models.IntegerField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    # choice Field
    food_category_CHOICES = (
        ('bunsik', '분식'),
        ('korean', '한식'),
        ('western', '양식'),
        ('hambuger', '햄버거'),
        ('salad', '샐러드'),
        ('dessert', '디저트'),
        ('chicken', '치킨'),
        ('bread', '빵'),
    )
    food_category = models.CharField(max_length=20, choices=food_category_CHOICES, default='bunsik')


    

    def __str__(self):
        return self.title

class Reply(models.Model):
    def __str__(self):
        return self.text

    lobby_id = models.ForeignKey(Lobby, on_delete=models.CASCADE, related_name='replys',null = True)
    text = models.CharField(max_length=100)

