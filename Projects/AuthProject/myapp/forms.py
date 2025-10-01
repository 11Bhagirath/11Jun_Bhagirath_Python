from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields='__all__'