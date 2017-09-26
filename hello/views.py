from django.shortcuts import render, get_object_or_404
from django.views import generic

from post.models import Product

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.order_by('-date')[:20]
