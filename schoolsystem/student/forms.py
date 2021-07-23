from django import forms
from django.forms import fields
from .model import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        models=Student
    Field= "__all__"