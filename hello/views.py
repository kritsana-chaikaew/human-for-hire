from django.shortcuts import render
from django.views import generic
from post.models import Product
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.utils import timezone
from django.http import HttpResponse

class IndexView(generic.ListView):
    template_name = 'hello/index.html'
    context_object_name = 'product_list'

    def post(self, request, *args, **kwargs):
        card = Product.objects.order_by('-init_date')
        if(request.method == 'POST'):
            card = card.filter(product_name=request.POST['gender'])
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
