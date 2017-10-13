from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from post.models import Product
from signupLogin.models import Profile
from .models import Order


def buy(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        product = Product.objects.get(id=request.product_no)
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        detail = request.POST['detail']
        location = request.POST['location']
        price = request.POST['price']
        #bankaccount = request.POST['bankaccount']
        
        o = Order()
        o.buyer_username = user
        o.product_no = product
        o.start_date = start_date
        o.end_date = end_date
        o.detail = detail
        o.location = location
        o.price = price
        o.save()
        return render(request,'buy_success.html',{})
    return render(request,'order.html',{})
