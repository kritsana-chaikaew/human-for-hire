from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telephone = models.CharField(max_length=200, blank=True)
    address = models.TextField(max_length=500, blank=True)
    GENDER = (
            ('male', 'Male'),
            ('female', 'Female'),
        )
    gender = models.CharField(max_length=10, choices=GENDER)
    birthday = models.DateField()
    card = models.CharField(max_length=16, blank=True)
    bank = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to='userImage', blank=True)
    buy_rating = models.FloatField(default=0)
    buy_rating_count = models.FloatField(default=0)
    sell_rating = models.FloatField(default=0)
    sell_rating_count = models.FloatField(default=0)


    def __str__(self):
        return str(self.user)

    def get_age(self):
        return timezone.now().year - self.birthday.year

    def get_buy_rating(self):
        star = [1]*int(self.buy_rating)
        if self.buy_rating%1 >= 0.5:
            star.append(0.5)
        star.extend([0]*(5-len(star)))
        return star

    def get_sell_rating(self):
        star = [1]*int(self.sell_rating)
        if self.sell_rating%1 >= 0.5:
            star.append(0.5)
        star.extend([0]*(5-len(star)))
        return star
