from django.db import models
from datetime import datetime
# Create your models here.

class Userinfo(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    state_news = models.TextField(blank=True)
    city_news = models.TextField(blank=True)
    bestpick_news = models.TextField(blank=True)
    last_date = models.DateTimeField(default = datetime.today)
    key_words = models.TextField(default='[]')

    def __str__(self):
        return self.username


class News(models.Model):
    date = models.DateTimeField()
    indian_news = models.TextField()
    national_news = models.TextField()
    international_news = models.TextField()
    bollywood_news = models.TextField()
    lifestyle_news = models.TextField()
    sport_news = models.TextField()
    business_news = models.TextField()
    sharemarket_news = models.TextField()
    corona_news = models.TextField()
    space_news = models.TextField()
    motivation_news = models.TextField()

    def __str__(self):
        return "daily_news"