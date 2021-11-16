from django import forms
from . import models

class CreateSignup (forms.ModelForm):
    class Meta:
        model = models.User_signup
        fields = ['name', 'lastname','phonenumber', 'address', 'gender']
