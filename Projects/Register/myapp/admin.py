from django.contrib import admin
from .models import *

# Register your models here.

class userdata(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','middlename','lastname','username','state','city','email','password','confirmpassword']

admin.site.register(userinfo, userdata)