from django import forms
from .models import *

class Signupform(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'
        
class Notesform(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','category','notesfile','desc']