from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

from taggit.managers import TaggableManager

class Product(models.Model):
    product_no = models.AutoField(primary_key=True)
    seller_username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=250, default='product name')
    product_image = models.ImageField(upload_to='img')
    product_details = models.CharField(max_length=2000, default='product details')
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=250, default='location')
    tags = TaggableManager(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    init_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.product_no) + "_" + self.product_name
