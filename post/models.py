# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    product_no = models.IntegerField(primary_key=True)

    seller_username = models.CharField(max_length=20, blank=True)
    product_name = models.CharField(max_length=250, blank=True)
    product_type = models.CharField(max_length=250, blank=True)
    date = models.DateField(blank=True)
    product_details = models.CharField(max_length=2000, blank=True)
    price = models.IntegerField(blank=True)
    tag = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return str(self.product_no) + "_" + self.product_name
