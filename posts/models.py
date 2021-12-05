from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    restaurant_name = models.CharField(max_length=255)
    eval = models.FloatField()
    content = models.CharField(max_length=255)
    date_of_post = models.DateTimeField(default=timezone.now)
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'Restaurante {self.restaurant_name}, nota: {self.eval}'


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'