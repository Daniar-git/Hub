from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    passw = models.CharField(max_length=20, validators=[MinLengthValidator(6)])
    login = models.CharField(max_length=50)
