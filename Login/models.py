from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


# Create your models here.

class UserManager(models.Manager):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

    def males(self):
        return self.all().filter(gender=self.GENDER_MALE)

    def females(self):
        return self.all().filter(gender=self.GENDER_FEMALE)


def __str__(self):
    return self.name


class User_signup(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    #birthday = models.DateTimeField(default=timezone.now, blank=True, null=True)
    phonenumber = models.CharField(max_length=20)
    address = models.TextField()
    gender = models.IntegerField(choices=UserManager.GENDER_CHOICES)
