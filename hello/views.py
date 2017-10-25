from django.shortcuts import render
from django.views import generic
from post.models import Product
from signupLogin.models import Profile
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.utils import timezone
from django.http import HttpResponse
import datetime

class IndexView(generic.ListView):
    template_name = 'hello/index.html'
    context_object_name = 'product_list'

    def post(self, request, *args, **kwargs):
        card = Product.objects.order_by('-init_date')
        if(request.method == 'POST'):
            gender = request.POST['gender']
            first_age = request.POST['first_age']
            end_age = request.POST['end_age']
            first_date = request.POST['first_date']
            end_date = request.POST['end_date']

            if gender != "":
                profile = Profile.objects.filter(gender=gender)
                user = User.objects.filter(profile__in=profile)
                card = card.filter(seller_username__in=user)
            if first_age != "":
                max_date = datetime.date.today()
                max_date = max_date.replace(year=max_date.year - int(first_age))
                profile = Profile.objects.filter(birthday__lte=max_date)
                user = User.objects.filter(profile__in=profile)
                card = card.filter(seller_username__in=user)
            if end_age != "":
                min_date = datetime.date.today()
                min_date = min_date.replace(year=min_date.year - int(end_age))
                profile = Profile.objects.filter(birthday__gte=min_date)
                user = User.objects.filter(profile__in=profile)
                card = card.filter(seller_username__in=user)
            if first_date != "":
                card = card.filter(start_date__gte=first_date)
            if end_date != "":
                card = card.filter(end_date__lte=end_date)

        args = {'product_list': card}
        return render(request, 'hello/index.html', args)

    def get_queryset(self):
        card = Product.objects.order_by('-init_date')
        return card


class ProductDetailView(generic.DetailView):
    template_name = 'hello/product_detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()

    def get_object(self):
        object = super(ProductDetailView, self).get_object()

        object.last_accessed = timezone.now()
        object.save()

        return object
