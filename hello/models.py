# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    product_no = models.IntegerField(primary_key=True)
    seller_username = models.CharField(max_length=20)
    product_name = models.CharField(max_length=250)
    product_type = models.CharField(max_length=250)
    product_details = models.CharField(max_length=2000)
    date = models.DateField()
    price = models.IntegerField()
    tag = models.CharField(max_length=250)
