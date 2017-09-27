# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Product
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select a file',
    )
# class ImageUploadForm(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField()

# Create your views here.
def post(request):
    return render(request,'post.html',{})

def action(request):
    p = Product()
    p.seller_username = "fetch from database"

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            p.product_image = request.FILES['product_image']
            p.product_image.save()
    # form = ImageUploadForm(request.POST, request.FILES)
    # p.product_image = form.cleaned_data['product_image']
    # p.product_image = request.POST['product_image']

    p.product_name = request.POST['product_name']
    p.start_date = request.POST['start_date']
    p.end_date = request.POST['end_date']
    p.product_details = request.POST['product_details']
    p.price = request.POST['price']
    p.tag = request.POST['tag']

    p.save()
    return render(request,'test.html',{})
