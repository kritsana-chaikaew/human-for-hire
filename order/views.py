from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from post.models import Product
from signupLogin.models import Profile
from .models import Order

from enum import Enum

TO_BE_ACCEPTED = 0
WAITING_FOR_WORK = 1
WAIT_BUYER_MARK_DONE = 2
WAIT_SELLER_MARK_DONE = 3
WORK_DONE_NOT_RATE = 4
WORK_DONE_RATED = 5
FAILED = 6
CANCELLED = 7

def buy(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        product = Product.objects.get(product_no=pk)
        seller_user = product.seller_username
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        detail = request.POST['detail']
        location = request.POST['location']
        price = request.POST['price']
        # bankaccount = request.POST['bankaccount']

        o = Order()
        o.buyer_username = user
        o.seller_username = seller_user
        o.product_no = product
        o.start_date = start_date
        o.end_date = end_date
        o.detail = detail
        o.location = location
        o.price = price
        o.status = TO_BE_ACCEPTED
        o.save()
        return render(request,'order/buy_success.html',{})
    return render(request,'order/order.html',{})

class WorkView(generic.ListView):
    template_name = 'order/manage_work.html'
    context_object_name = 'work_list'

    def get_queryset(self):
        return Order.objects.filter(seller_username=self.request.user.id)

class HiredView(generic.ListView):
    template_name = 'order/manage_hired.html'
    context_object_name = 'work_list'

    def get_queryset(self):
        return Order.objects.filter(buyer_username=self.request.user.id)

def accept_work(request):
    data = {
        'success': True
    }
    try:
        o = Order.objects.get(order_no=request.GET.get('order_no'))
        o.status = WAITING_FOR_WORK;
        o.save()
    except:
        data['success'] = False
    return JsonResponse(data)

def seller_confirm_workdone(request):
    data = {
        'success': True
    }
    try:
        o = Order.objects.get(order_no=request.GET.get('order_no'))
        print("hie")
        print(o.status)
        if o.status == WAITING_FOR_WORK:
            o.status = WAIT_BUYER_MARK_DONE
        elif o.status == WAIT_SELLER_MARK_DONE:
            o.status = WORK_DONE_NOT_RATE
        else:
            raise ValueError('Can not be done.')
        o.save()
    except:
        data['success'] = False
    return JsonResponse(data)

def buyer_confirm_workdone(request):
    data = {
        'success': True
    }
    try:
        o = Order.objects.get(order_no=request.GET.get('order_no'))
        print(o.status)
        if o.status == WAITING_FOR_WORK:
            o.status = WAIT_SELLER_MARK_DONE
        elif o.status == WAIT_BUYER_MARK_DONE:
            o.status = WORK_DONE_NOT_RATE
        else:
            raise ValueError('Can not be done.')
        o.save()
    except:
        data['success'] = False
    return JsonResponse(data)

def cancel_work(request):
    data = {
        'success': True
    }
    try:
        o = Order.objects.get(order_no=request.GET.get('order_no'))
        o.status = CANCELLED;
        o.save()
    except:
        data['success'] = False
    return JsonResponse(data)

def rate_employee(request, order_no, username):
    request.session['order_no'] = order_no
    request.session['username'] = username
    print(request.session['order_no'])
    print(request.session['username'])

    if request.method == 'POST':
        print(request.POST['rating'])
    return render(request,'order/rate_employee.html',{})

def rate_employer(request, order_no, username):
    request.session['order_no'] = order_no
    request.session['username'] = username
    print(request.session['order_no'])
    print(request.session['username'])

    if request.method == 'POST':
        print(request.POST['rating'])
    return render(request,'order/rate_employer.html',{})
