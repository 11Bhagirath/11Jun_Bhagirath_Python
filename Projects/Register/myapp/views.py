from django.shortcuts import render,redirect
from .forms import *
from.models import userinfo

# Create your views here.

def index(request):
    data=userinfo.objects.all()
    print(data)
    return render(request,'index.html', {'data':data})

def register(request):
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted!")
        else:
            print(form.errors)
    return render(request,'register.html')

def update(request,id):
    uid=userinfo.objects.get(id=id)
    if request.method =='POST':
        form = updateform(request.POST,instance=uid)
        if form.is_valid():
            form.save()
            print("Record Updated!")
            return redirect('index')
        else:
            print(form.errors)
    return render(request, 'update.html',{'uid':uid})
