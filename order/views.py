from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from post.models import Product
from signupLogin.models import Profile
from .models import Order

from signupLogin.models import Profile

import base64
import urllib.parse

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

@login_required(login_url='/login')
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
        # payment = request.POST['payment']

        if int(price) < 0:
            error = 'The price can\'t be negative'
            return render(request, 'order/order.html', {'seller_user': seller_user, 'start_date':start_date, 'end_date':end_date, 'detail':detail, 'location':location, 'price':price, "error":[error]})



        o = Order()
        o.buyer_username = user
        o.seller_username = seller_user
        o.product_no = product
        o.start_date = start_date
        o.end_date = end_date
        o.detail = detail
        o.location = location
        o.price = price
        o.status = Order.TO_BE_ACCEPTED
        o.save()
        return render(request,'order/buy_success.html',{})

    product = Product.objects.get(product_no=pk)
    seller_user = product.seller_username
    args = {'seller_user': seller_user}
    return render(request,'order/order.html', args)

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
        o.status = Order.WAITING_FOR_WORK;
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
        print("status seller_confirm_workdone: " + str(o.status))
        if o.status == Order.WAITING_FOR_WORK:
            print('aaaaaaaa')
            o.status = Order.WAIT_BUYER_MARK_DONE
        elif o.status == Order.WAIT_SELLER_MARK_DONE:
            print('bbbbbbbb')
            o.status = Order.WORK_DONE
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
        print("status buyer_confirm_workdone: " + str(o.status))
        if o.status == Order.WAITING_FOR_WORK:
            print('aaaaaaaa')
            o.status = Order.WAIT_SELLER_MARK_DONE
        elif o.status == Order.WAIT_BUYER_MARK_DONE:
            print('bbbbbbbb')
            o.status = Order.WORK_DONE
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
        o.status = Order.CANCELLED;
        o.save()
    except:
        data['success'] = False
    return JsonResponse(data)

def rate_employee(request, order_no):
    request.session['order_no'] = order_no
    request.session['user_type'] = 'employee'
    return redirect('/rate/')

def rate_employer(request, order_no):
    request.session['order_no'] = order_no
    request.session['user_type'] = 'employer'
    return redirect('/rate/')

def rate(request):
    try:
        order_no = request.session['order_no']
        user_type = request.session['user_type']
    except:
        order_no = None
        user_type = None

    if order_no == None:
        return render(request, 'order/fail.html', {'message':'Do not access link without clicking button...'})

    print('order_no: ' + order_no)

    try:
        order_no = str(int((int(base64ToString(urllib.parse.unquote(order_no))) + 5555) / 9876))
        print('order_no: ' + order_no)
        od = Order.objects.get(order_no=order_no)
    except:
        request.session['order_no'] = None
        request.session['user_type'] = None
        return render(request, 'order/fail.html', {'message':"Don't try to hack url..."})


    if user_type == 'employee':
        who = od.seller_username
        who_pf = Profile.objects.get(user=od.seller_username)
        product_name = od.product_no.product_name
        image = od.product_no.product_image
        detail = od.product_no.product_details
        rating = who_pf.sell_rating
    elif user_type == 'employer':
        who = od.buyer_username
        who_pf = Profile.objects.get(user=od.buyer_username)
        product_name = ''
        image = who_pf.image
        detail = od.detail
        rating = who_pf.buy_rating


    if request.method == 'POST':
        score = int(request.POST['rating'])
        if user_type == 'employee':
            pf = Profile.objects.get(user=od.seller_username)
            pf.sell_rating = ((pf.sell_rating * pf.sell_rating_count) + score) / (pf.sell_rating_count + 1)
            pf.sell_rating_count = pf.sell_rating_count + 1
            pf.save()
            try:
                o = Order.objects.get(order_no=order_no)
                if o.status == Order.WAITING_FOR_WORK:
                    o.status = Order.WAIT_SELLER_MARK_DONE
                elif o.status == Order.WAIT_BUYER_MARK_DONE:
                    o.status = Order.WORK_DONE
                o.save()
            except:
                print('cannot rate employee')
        if user_type == 'employer':
            pf = Profile.objects.get(user=od.buyer_username)
            pf.buy_rating = ((pf.buy_rating * pf.buy_rating_count) + score) / (pf.buy_rating_count + 1)
            pf.buy_rating_count = pf.buy_rating_count + 1
            pf.save()
            try:
                o = Order.objects.get(order_no=order_no)
                if o.status == Order.WAITING_FOR_WORK:
                    o.status = Order.WAIT_BUYER_MARK_DONE
                elif o.status == Order.WAIT_SELLER_MARK_DONE:
                    o.status = Order.WORK_DONE
                o.save()
            except:
                print('cannot rate employer')


        request.session['order_no'] = None
        request.session['user_type'] = None


        if user_type == 'employee':
            return redirect('/manage-hired')
        if user_type == 'employer':
            return redirect('/manage-work')


    args = {'user_type': user_type, 'username': who, 'product_name': product_name, 'image': image, 'detail': detail, 'rating': rating}
    return render(request, 'order/rate.html', args)

def rate_wrong_url(request):
    return render(request, 'order/fail.html', {'message':"Sorry, wrong url..."})
