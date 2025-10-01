from django.shortcuts import render,redirect
from .forms import * 
from django.contrib.auth import logout
import random
from django.core.mail import send_mail
from FianlProject import settings

# Create your views here.

def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

def notes(request):
    user=request.session.get("user")
    email=usersignup.objects.get(email=user)
    if request.method=='POST':
        form=Notesform(request.POST,request.FILES)
        if form.is_valid():
            temp=form.save(commit=False)
            temp.status="Pending"
            temp.email=email
            temp.save()
            print("Notes Submitted!")
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'notes.html')

def profile(request):
    userid=request.session.get("userid")
    cuser=usersignup.objects.get(id=userid)
    if request.method=='POST':
        form=Signupform(request.POST,instance=cuser)
        if form.is_valid(): 
            form.save() 
            msg="Update Successfully!"
            return redirect('/')
            
        else:
            print(form.errors)
            
    return render(request,'profile.html',{'userid':cuser})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

otp=0

def signup(request):
    msg=""
    if request.method=='POST':
        form=Signupform(request.POST)
        if form.is_valid(): 
            form.save() 
            msg="Signup Successfully!"
            
            #Otp Sending Code
            global otp
            otp=random.randint(111111,999999)   
            sub="Your One Time Password"
            message=f"Dear User!\n\nThanks for registering our service!\n\nFor account verification, Your one time password is {otp}.\n\nThanks & Regards\n\nNotesApp\n\n+917359507546 | bhagirath.patel7546@gmail.com"
            from_email=settings.EMAIL_HOST_USER
            to_email=[request.POST["email"]]
            
            send_mail(subject=sub,message=message,from_email=from_email,recipient_list=to_email)
            
            print("Email Sent successfully!")
            return redirect('otpverify')
        else:
            print(form.errors)
            msg="Error! Something Went Wrong..."
    return render(request,'signup.html',{'msg':msg})

def login(request):
    msg=""
    if request.method=='POST':
        email=request.POST['email']
        pas=request.POST['password']
        
        user=usersignup.objects.filter(email=email,password=pas)
        userid=usersignup.objects.get(email=email)
        if user: #True
            msg="Login Successfull!"
            print("Login Successfull!")
            request.session["user"]=email
            request.session["userid"]=userid.id
            
            return redirect('/')
        else:
            print("Error! Login Failed...")
            msg="Error! Login Failed..."
    return render(request,'login.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('login')

def otpverify(request):
    global otp
    print(otp)
    if request.method=='POST':
        myotp=request.POST['otp']
        if otp==int(myotp):
            print("OTP Verified!")
            return redirect("login")
        else:
            print("OTP Verification Failed...Try Again! ")
    return render(request,'otpverify.html')