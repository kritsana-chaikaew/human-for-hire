from __future__ import unicode_literals
<<<<<<< HEAD
=======

from django.db import models
import datetime

class Product(models.Model):
    product_no = models.IntegerField(primary_key=True)
    seller_username = models.CharField(max_length=20)
    product_name = models.CharField(max_length=250)
    product_type = models.CharField(max_length=250)
    product_details = models.CharField(max_length=2000)
    date = models.DateField()
    price = models.IntegerField()
    tag = models.CharField(max_length=250)

    def __str__(self):
        return str(self.product_no) + "_" + self.product_name
>>>>>>> 67aa83401e7116fe394454779470147ef6e44926
