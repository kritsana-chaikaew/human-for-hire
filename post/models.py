# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    product_no = models.IntegerField(primary_key=True)

    seller_username = models.CharField(max_length=250, default='seller_username')
    product_image = models.ImageField(upload_to='post/upload/image')
    product_name = models.CharField(max_length=250, default='product name')
    product_type = models.CharField(max_length=250, default='product type')
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    product_details = models.CharField(max_length=2000, default='product details')
    location = models.CharField(max_length=250, default='location')
    price = models.IntegerField(default=0)
    tag = models.CharField(max_length=250, default='tag')

    def __str__(self):
        return str(self.product_no) + "_" + self.product_name
