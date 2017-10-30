from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telephone = models.CharField(max_length=200, blank=True)
    address = models.TextField(max_length=500, blank=True)
    gender = models.TextField(max_length=10, blank=True)
    birthday = models.DateField()
    bankaccount = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='userImage', blank=True)

    def __str__(self):
        return str(self.user)
