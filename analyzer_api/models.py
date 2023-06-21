from django.db import models



class Sentiment(models.Model):

    text = models.TextField()
    sentiment = models.CharField(max_length=10) 
