from django.db import models

# Create your models here.

class usersignup(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    mobile=models.BigIntegerField()
    
class Notes(models.Model):
    submitted_at=models.DateTimeField(auto_now=True)
    email= models.ForeignKey(usersignup,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    notesfile=models.FileField(upload_to='NotesData')
    desc=models.TextField()
    statuschoice=[
        ('Pending','Pending'),
        ('Approve','Approve'),
        ('Reject','Reject'),
    ]
    status=models.CharField(choices=statuschoice,max_length=20)
    updated_at=models.DateField(blank=True,null=True)