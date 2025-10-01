from django.db import models

# Create your models here.

class userinfo(models.Model):
    name=models.CharField(max_length=20)
    middlename=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.TextField()
    state=models.TextField()
    city=models.TextField()
    email=models.EmailField()
    password=models.TextField()
    confirmpassword=models.TextField()