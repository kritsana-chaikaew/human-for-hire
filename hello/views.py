from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from post.models import Product

class IndexView(generic.ListView):
    template_name = 'hello/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.order_by('-init_date')

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
