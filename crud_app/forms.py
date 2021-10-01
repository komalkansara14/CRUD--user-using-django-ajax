from django import forms
from django.forms import widgets
from .models import User

class UserRegistrationForm(forms.ModelForm):
 class Meta:
  model = User
  fields = ['name', 'email', 'department']
  widgets = {
    'name': forms.TextInput(attrs={'class': 'form-control', 'id':'nameid'}),
    'email': forms.EmailInput(attrs={'class': 'form-control', 'id':'emailid'}),
    'department': forms.TextInput(attrs={'class': 'form-control', 'id':'deptid'}),

  }