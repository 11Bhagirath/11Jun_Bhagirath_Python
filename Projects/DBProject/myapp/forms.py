from django import forms
from .models import * 

class userform(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'

class updateform(forms.ModelForm):
    class Meta:
        model=userinfo
        fields=['name','email','dob','mobile']