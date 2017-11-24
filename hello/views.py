from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime

from post.models import Product
from taggit.models import Tag
from signuplogin.models import Profile

import json
from functools import reduce
import operator
from django.db.models import Q

CARDS_PER_PAGE = 8

def filter(cards, gender, first_age, end_age, first_date, end_date, tag_list, sort):
    if gender != "":
        print("gender")
        profile = Profile.objects.filter(gender=gender)
        user = User.objects.filter(profile__in=profile)
        cards = cards.filter(seller_username__in=user)
    if first_age != "":
        print("fage")
        max_date = datetime.date.today()
        max_date = max_date.replace(year=max_date.year - int(first_age))
        profile = Profile.objects.filter(birthday__lte=max_date)
        user = User.objects.filter(profile__in=profile)
        cards = cards.filter(seller_username__in=user)
    if end_age != "":
        print("lage")
        min_date = datetime.date.today()
        min_date = min_date.replace(year=min_date.year - int(end_age))
        profile = Profile.objects.filter(birthday__gte=min_date)
        user = User.objects.filter(profile__in=profile)
        cards = cards.filter(seller_username__in=user)
    if first_date != "":
        print("fdate")
        cards = cards.filter(start_date__gte=first_date)
    if end_date != "":
        print("ldate")
        cards = cards.filter(end_date__lte=end_date)
    if tag_list != ['']:
        print(tag_list)
        cards = cards.filter(tags__name__in=tag_list)

    if sort == 'rating':
        cards = cards.distinct().order_by('-seller_username__profile__sell_rating')
    else:
        cards = cards.distinct().order_by('-init_date')

    return cards

class IndexView(generic.ListView):
    template_name = 'hello/index.html'
    context_object_name = 'product_list'

    def post(self, request, *args, **kwargs):
        cards = Product.objects

        if(request.method == 'POST'):
            gender = request.POST['gender']
            age = request.POST['age']
            age = age.split(',')
            first_age = age[0]
            end_age = age[1]
            first_date = request.POST['first_date']
            end_date = request.POST['end_date']
            tag_list = request.POST['tag_list']
            tag_list = request.session['tag_list'] = tag_list.split(',')
            sort = request.session['sort'] = request.POST['sort']
            cards = filter(cards, gender, first_age, end_age, first_date, end_date, tag_list, sort)

        page = request.GET.get('page', 1)
        paginator = Paginator(cards, CARDS_PER_PAGE)
        try:
            product_list = paginator.page(page)
        except PageNotAnInteger:
            product_list = paginator.page(1)
        except EmptyPage:
            product_list = paginator.page(paginator.num_pages)

        return render(request, 'hello/index.html', {'product_list': product_list})

    def get_queryset(self):
        cards = Product.objects.order_by('-init_date')
        page = self.request.GET.get('page', 1)
        if int(page) == 1:
            self.request.session['gender'] = ""
            self.request.session['first_age'] = ""
            self.request.session['end_age'] = ""
            self.request.session['first_date'] = ""
            self.request.session['end_date'] = ""
            self.request.session['tag_list'] = ['']
            self.request.session['sort'] = ""
        elif int(page) >= 2:
            gender = self.request.session['gender']
            first_age = self.request.session['first_age']
            end_age = self.request.session['end_age']
            first_date = self.request.session['first_date']
            end_date = self.request.session['end_date']
            tag_list = self.request.session['tag_list']
            sort = self.request.session['sort']
            cards = filter(cards, gender, first_age, end_age, first_date, end_date, tag_list, sort)

        paginator = Paginator(cards, CARDS_PER_PAGE)
        try:
            product_list = paginator.page(page)
        except PageNotAnInteger:
            product_list = paginator.page(1)
        except EmptyPage:
            product_list = paginator.page(paginator.num_pages)

        return product_list


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
