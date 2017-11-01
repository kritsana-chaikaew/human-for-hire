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

TO_BE_ACCEPTED = 0
WAITING_FOR_WORK = 1
WAIT_BUYER_MARK_DONE = 2
WAIT_SELLER_MARK_DONE = 3
WORK_DONE_NOT_RATE = 4
WORK_DONE_RATED = 5
FAILED = 6
CANCELLED = 7

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

    if order_no != None:
        od = Order.objects.get(order_no=order_no)
    else:
        return render(request, 'order/fail.html')


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
        if user_type == 'employer':
            pf = Profile.objects.get(user=od.buyer_username)
            pf.buy_rating = ((pf.buy_rating * pf.buy_rating_count) + score) / (pf.buy_rating_count + 1)
            pf.buy_rating_count = pf.buy_rating_count + 1
            pf.save()

        request.session['order_no'] = None
        request.session['user_type'] = None

        if user_type == 'employee':
            return redirect('/manage-hired')
        if user_type == 'employer':
            return redirect('/manage-work')


    args = {'user_type': user_type, 'username': who, 'product_name': product_name, 'image': image, 'detail': detail, 'rating': rating}
    return render(request, 'order/rate.html', args)
