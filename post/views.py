# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Product
# Create your views here.
def post(request):
    return render(request,'post.html',{})

def action(request):
    p = Product()
    p.seller_username = request.POST['seller_name']
    p.product_name = request.POST['product_name']
    p.product_type = request.POST['product_type']
    p.start_date = request.POST['start_date']
    p.end_date = request.POST['end_date']
    p.product_details = request.POST['product_details']
    p.price = request.POST['price']
    p.tag = request.POST['tag']

    p.save()
    return render(request,'test.html',{})
