from django.db import models

# Create your models here.

class NewsDetails(models.Model):
    news_details = models.JSONField()