from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout


# Create your views here.

def index(request):
    msg=""
    if request.method=='POST':
        unm=request.POST['email']
        pas=request.POST['password']
        
        user=Signup.objects.filter(email=unm,password=pas)
        if user: #TRUE
            print("Login Successfull!")
            msg="Login Successfull!"
            
            #Gen. Session
            request.session["user"]=unm
            return redirect('home')
        else:
            print("Error!Login Failed...")
            msg="Error!Login Failed..."
        
    return render(request,'index.html',{'msg':msg})

def register(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'register.html')

def home(request):
    user=request.session.get("user")
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

