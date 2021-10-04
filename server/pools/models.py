from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Pool(models.Model):
    name = models.CharField(max_length=30)
    max_entries = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(5)])