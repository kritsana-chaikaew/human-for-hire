from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telephone = models.CharField(max_length=200, blank=True)
    address = models.TextField(max_length=500, blank=True)
    GENDER = (
            ('male', 'Male'),
            ('female', 'Female'),
        )
    gender = models.CharField(max_length=10, choices=GENDER)
    birthday = models.DateField(default=datetime.date.today)
    bankaccount = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='userImage', blank=True)
    buy_rating = models.FloatField(default=0)
    buy_rating_count = models.FloatField(default=0)
    sell_rating = models.FloatField(default=0)
    sell_rating_count = models.FloatField(default=0)


    def __str__(self):
        return str(self.user)

    def get_age(self):
        return datetime.datetime.now().year - self.birthday.year

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
