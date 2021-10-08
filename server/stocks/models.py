from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    price = models.IntegerField()
