from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    if request.method=='POST': #True
        form = userform(request.POST)
        if form.is_valid(): #True
           form.save()
           print("Record Inserted!")
        else:
           print(form.errors)   
    return render(request,'index.html')

def showdata(request):
    data=userinfo.objects.all()
    print(data)
    return render(request,'showdata.html', {'data': data})

def updatedata(request,id):
    uid=userinfo.objects.get(id=id)
    if request.method=='POST': #True
        form = updateform(request.POST,instance=uid)
        if form.is_valid(): #True
           form.save()
           print("Record Update!")
           return redirect('showdata')
        else:
           print(form.errors)  
    return render(request, 'updatedata.html',{'uid':uid})

def deletedata(request,id):
    uid=userinfo.objects.get(id=id)
    userinfo.delete(uid)
    return redirect('showdata')