from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices = (
        ('job_seeker','Job Seeker'),
        ('employer','Employer')
    ),widget=forms.RadioSelect)
    class Meta:
        model = User
        fields = ('username','email','role','password1','password2')


