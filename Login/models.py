from django.db import models
from django.contrib.auth.models import User
from datetime import date


#Create your models here.

class UserManager(models.Manager):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    def males(self):
        return self.all().filter(gender=self.GENDER_MALE)
    def females(self):
        return self.all().filter(gender=self.GENDER_FEMALE)

# class Article(models.Model):
#     name = models.CharField()
#     lastname = models.CharField()
#     birthday = models.DateTimeField()
#     phonenumber = models.IntegerField
#     address = models.TextField
#     # gender= models.TextChoices()
#     # gender= models.BooleanField(default=False)
#     gender = models.IntegerField(choices=UserManager.GENDER_CHOICES)

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #image= models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

def __str__(self):
    return self.name

def snippet(self):
    return self.body[:50] + " ..."


class User_signup(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    #birthday = models.DateTimeField(null=True)
    phonenumber = models.CharField(max_length=20)
    address = models.TextField()
    gender = models.IntegerField(choices=UserManager.GENDER_CHOICES)
