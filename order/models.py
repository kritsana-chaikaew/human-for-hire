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
    purchase_date = models.DateTimeField(default=datetime.datetime.now())
    location = models.CharField(max_length=250, default='location')
    price = models.IntegerField(default=0)
    detail = models.CharField(max_length=250, default='datail')
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=datetime.datetime.now())

    TO_BE_ACCEPTED = 0
    WAITING_FOR_WORK = 1
    WAIT_BUYER_MARK_DONE = 2
    WAIT_SELLER_MARK_DONE = 3
    # WORK_DONE_NOT_RATE = 4
    # WORK_DONE_RATED = 5
    WORK_DONE_RATED = 4
    FAILED = 5
    CANCELLED = 6
    STATUS_CODE_CHOICES = (
            (TO_BE_ACCEPTED, 'TO BE ACCEPTED'),
            (WAITING_FOR_WORK, 'WAITING FOR WORK'),
            (WAIT_BUYER_MARK_DONE, 'WAIT BUYER MARK DONE'),
            (WAIT_SELLER_MARK_DONE, 'WAIT SELLER MARK DONE'),
            # (WORK_DONE_NOT_RATE, 'WORK DONE NOT RATED'),
            # (WORK_DONE_RATED, 'WORK DONE RATED'),
            (WORK_DONE_RATED, 'WORK DONE'),
            (FAILED, 'FAILED'),
            (CANCELLED, 'CANCELLED'),
        )
    status = models.PositiveSmallIntegerField(choices=STATUS_CODE_CHOICES, default=TO_BE_ACCEPTED)

    def __str__(self):
        return str(self.order_no) + '_' + str(self.buyer_username)

    def get_seller_username(self):
        return self.product_no.seller_username
