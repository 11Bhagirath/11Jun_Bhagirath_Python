from django.db import models

# Create your models here.

class Usersignup(models.Model):
    signup_at=models.DateTimeField(auto_now=True)
    fullname=models.CharField(max_length=50)
    usernme=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    mobile=models.BigIntegerField()
