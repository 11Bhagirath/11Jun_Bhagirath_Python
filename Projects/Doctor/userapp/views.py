from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from Doctor import settings

# Create your views here.

def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

def profile(request):
    return render(request,'profile.html')

def contact(request):
    return render(request,'contact.html')

def signup(request):
    msg=""
    if request.method=='POST':
        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            msg="Login Successfull!"
            return redirect('login')
        else:
            print(form.errors)
    return render(request,'signup.html',{'msg':msg})

def login(request):
    msg=""
    if request.method=='POST':
        username=request.POST['username']
        pas=request.POST['password']
        
        user=Usersignup.objects.filter(username=username,password=pas)
        userid=Usersignup.objects.get(username=username)
        if user: #True
            msg="Login Successful!"
            request.session["user"]=username
            request.session["userid"]=userid.id
            
            return redirect('/')
        else:
            print("ERROR!")
            msg="Error! Login Failed...."
    return render(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect('login')
