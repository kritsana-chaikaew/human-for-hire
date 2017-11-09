from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone

import datetime

from post.models import Product
from taggit.models import Tag
from signupLogin.models import Profile

import json
from functools import reduce
import operator
from django.db.models import Q

class IndexView(generic.ListView):
    template_name = 'hello/index.html'
    context_object_name = 'product_list'

    def post(self, request, *args, **kwargs):
        cards = Product.objects.order_by('-init_date')
        if(request.method == 'POST'):
            gender = request.POST['gender']
            first_age = request.POST['first_age']
            end_age = request.POST['end_age']
            first_date = request.POST['first_date']
            end_date = request.POST['end_date']
            tag_list = request.POST['tag_list']
            tag_list = tag_list.split(',')

            if gender != "":
                profile = Profile.objects.filter(gender=gender)
                user = User.objects.filter(profile__in=profile)
                cards = cards.filter(seller_username__in=user)
            if first_age != "":
                max_date = datetime.date.today()
                max_date = max_date.replace(year=max_date.year - int(first_age))
                profile = Profile.objects.filter(birthday__lte=max_date)
                user = User.objects.filter(profile__in=profile)
                cards = cards.filter(seller_username__in=user)
            if end_age != "":
                min_date = datetime.date.today()
                min_date = min_date.replace(year=min_date.year - int(end_age))
                profile = Profile.objects.filter(birthday__gte=min_date)
                user = User.objects.filter(profile__in=profile)
                cards = cards.filter(seller_username__in=user)
            if first_date != "":
                cards = cards.filter(start_date__gte=first_date)
            if end_date != "":
                cards = cards.filter(end_date__lte=end_date)
            if tag_list != []:
                cards = cards.filter(tags__name__in=tag_list).distinct()

            cards = list(set(cards))

        args = {'product_list': cards}
        return render(request, 'hello/index.html', args)

    def get_queryset(self):
        cards = Product.objects.order_by('-init_date')
        return cards


class ProductDetailView(generic.DetailView):
    template_name = 'hello/product_detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()

    def get_object(self):
        object = super(ProductDetailView, self).get_object()

        object.last_accessed = timezone.now()
        object.save()

        return object

class TagResultView(generic.ListView):
    template_name = 'hello/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        product_list = Product.objects.order_by('-init_date')
        product_list = product_list.filter(tags__name__in=[self.kwargs['tags']]).distinct()

        return product_list

def get_tags(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        tags = Tag.objects.filter(name__icontains = q )[:20]
        results = []
        for tag in tags:
            tag_json = {}
            tag_json['id'] = tag.id
            tag_json['label'] = tag.name
            tag_json['value'] = tag.name
            results.append(tag_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
