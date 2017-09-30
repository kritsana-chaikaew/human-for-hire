# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.files.images import ImageFile

from django.contrib.auth.models import User
from .models import Product

def post(request):
    return render(request,'post.html',{})

def action(request):
    product = Product()
    user = User.objects.get(id=request.user.id)
    product.seller_username = user

    image_content = ImageFile(request.FILES['product_image'])
    product.product_image = image_content

    product.product_name = request.POST['product_name']
    product.start_date = request.POST['start_date']
    product.end_date = request.POST['end_date']
    product.product_details = request.POST['product_details']
    product.price = request.POST['price']
    product.location = request.POST['location']
    product.tag = request.POST['tag']

    product.save()
    return render(request,'post_respond.html',{})
