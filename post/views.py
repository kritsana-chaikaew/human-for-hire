from __future__ import unicode_literals

from django.shortcuts import render
from django.core.files.images import ImageFile

from django.contrib.auth.models import User
from .models import Product
from .forms import EditPostForm
from django.shortcuts import render, redirect

import taggit

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

    product.save()

    tag_list = taggit.utils._parse_tags(request.POST['tags'])
    product.tags.add(*tag_list)

    return render(request, 'post_respond.html', {})

def delete(request, pk):
    product = Product.objects.get(product_no=pk)
    if product:
        product.delete()

    return render(request, 'delete_respond.html', {})

def edit(request, pk):
    product = Product.objects.get(product_no=pk)
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return render(request, 'edit_response.html', {})

    else:
        form = EditPostForm(instance=product)
        args = {'form': form}
        return render(request, 'edit.html', args)
