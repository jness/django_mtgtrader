from django.db import models

class Decks(models.Model):
    hash = models.CharField(max_length=25, unique=True)
    data1 = models.CharField(max_length=1000)
    data2 = models.CharField(max_length=1000)
