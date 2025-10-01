from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Signup(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    mobile=models.BigIntegerField()