from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from post.models import Product
from signupLogin.models import Profile
from .models import Order


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
        o.status = 0
        o.save()
        return render(request,'order/buy_success.html',{})
    return render(request,'order/order.html',{})

class WorkView(generic.ListView):
    template_name = 'order/manage_work.html'
    context_object_name = 'work_list'

    def get_queryset(self):
        return Order.objects.filter(seller_username=self.request.user.id)

def accept_work(request):
    data = {
        'success': True
    }
    # try:
    #     o = Order.objects.get(order_no=request.GET.get('order_no'));
    #     o.status = 1;
    #     o.save()
    # except:
    #     data.success = False
    return JsonResponse(data)

def confirm_workdone(request):
    data = {
        'success': True
    }
    # try:
    #     o = Order.objects.get(order_no=request.GET.get('order_no'));
    #     o.status = 2;
    #     o.save()
    # except:
    #     data.success = False
    return JsonResponse(data)