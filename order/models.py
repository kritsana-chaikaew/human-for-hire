# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from post.models import Product
import datetime

# Create your models here.
class Order(models.Model):
    order_no = models.IntegerField(primary_key=True)
    product_no = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    buyer_username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='buyer')
    seller_username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='seller')
    purchase_date = models.DateTimeField(default=datetime.datetime.now())
    location = models.CharField(max_length=250, default='location')
    price = models.IntegerField(default=0)
    detail = models.CharField(max_length=250, default='datail')
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=datetime.datetime.now())
    STATUS_CODE = (
            (0, 'TO BE ACCEPTED'),
            (1, 'WAITING FOR WORK'),
            (2, 'WORK DONE'),
            (3, 'FAILED'),
            (4, 'CANCELLED')
        )
    status = models.PositiveSmallIntegerField(choices=STATUS_CODE, default=0)

    def __str__(self):
        return str(self.order_no) + '_' + str(self.buyer_username) 
