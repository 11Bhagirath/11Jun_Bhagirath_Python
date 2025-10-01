from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def categories(request):
    return render(request,'categories.html')

def contestdetails(request):
    return render(request,'contestdetails.html')

def contests(request):
    return render(request,'contests.html')

def users(request):
    return render(request,'users.html')
