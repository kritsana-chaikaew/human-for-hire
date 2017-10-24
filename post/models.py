# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    product_no = models.IntegerField(primary_key=True)

    seller_username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    product_image = models.ImageField(upload_to='img')
    product_name = models.CharField(max_length=250, default='product name')
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    product_details = models.CharField(max_length=2000, default='product details')
    location = models.CharField(max_length=250, default='location')
    price = models.IntegerField(default=0)
    tag = models.CharField(max_length=250, default='tag')
    init_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.product_no) + "_" + self.product_name
