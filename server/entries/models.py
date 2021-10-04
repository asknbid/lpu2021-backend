from django.db import models
from users.models import User
from pools.models import Pool
from stocks.models import Stock
import random

def generate_random_returns():
    return random.uniform(-5, 5)

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
    stocks = models.ManyToManyField(to=Stock)
    returns = models.FloatField(default=generate_random_returns)