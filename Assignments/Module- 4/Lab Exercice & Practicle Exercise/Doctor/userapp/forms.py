from django import forms
from .models import *

class Signupform(forms.ModelForm):
    class Meta:
        model=Usersignup
        fields=['fullname','usernme','email','password','mobile']