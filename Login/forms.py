from django import forms
from . import models


class CreateArticle (forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'body']

class CreateSignup (forms.ModelForm):
    class Meta:
        model = models.User_signup
        fields = ['name', 'lastname','phonenumber', 'address', 'gender']
