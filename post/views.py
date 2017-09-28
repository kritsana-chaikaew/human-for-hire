# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.files.images import ImageFile

from .models import Product

def post(request):
    return render(request,'post.html',{})

def action(request):
    p = Product()
    p.seller_username = "fetch from database"

    image_content = ImageFile(request.FILES['product_image'])
    p.product_image = image_content

    p.product_name = request.POST['product_name']
    p.start_date = request.POST['start_date']
    p.end_date = request.POST['end_date']
    p.product_details = request.POST['product_details']
    p.price = request.POST['price']
    p.tag = request.POST['tag']

    p.save()
    return render(request,'post_respond.html',{})
