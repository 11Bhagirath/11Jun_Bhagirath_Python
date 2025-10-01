from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [
    path('',views.index),
    path('notes/',views.notes,name='notes'),
    path('profile/',views.profile,name='profile'),
    path('about/',views.about,name='about'),
    path('conatct/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),  
    path('userlogout/',views.userlogout,name='userlogout'),
    path('otpverify/',views.otpverify,name='otpverify'),  
] 