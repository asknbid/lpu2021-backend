from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=10, validators=[MinLengthValidator(4)])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)