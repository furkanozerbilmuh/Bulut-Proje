from django.db import models
from django import forms


# Create your models here.

class user(models.Model):
    email = models.EmailField(primary_key=True)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    CHOICES = [('ogrenci','Öğrenci'),('egitmen','Eğitmen')]
    type = models.CharField(max_length=20, choices=CHOICES, default=1)

    def __str__(self):
        return self.email
