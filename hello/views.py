from django.shortcuts import render
from django.views import generic
from post.models import Product

class IndexView(generic.ListView):
    template_name = 'hello/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.order_by('-start_date')
