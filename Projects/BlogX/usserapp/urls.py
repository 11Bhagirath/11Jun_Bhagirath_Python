from django.contrib import admin
from django.urls import path,include
from usserapp import views

urlpatterns = [
    path('',views.index),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
]