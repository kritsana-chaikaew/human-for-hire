from django.shortcuts import render
from django.views import generic
from post.models import Product
from django.views.generic import DetailView
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'hello/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.order_by('-init_date').filter(product_details='1')

class ProductDetailView(generic.DetailView):
    template_name = 'hello/product_detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()

    def get_object(self):
        object = super(ProductDetailView, self).get_object()

        object.last_accessed = timezone.now()
        object.save()

        return object
