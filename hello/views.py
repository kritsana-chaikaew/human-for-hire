from django.shortcuts import render
from django.views import generic
from post.models import Product
from django.views.generic import DetailView
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'hello/index.html'
    context_object_name = 'product_list'
    # gender = request.POST['gender']
    # start_age = ""
    # end_age = ""
    # start_date = ""
    # end_date = ""

    # def filter_gender(self, gender):
    #     self.gender = gender

    def get_queryset(self):
        card = Product.objects.order_by('-init_date')
        # if self.gender != "":
        #     card = card.filter()
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

# def filter(request):
#     IndexView.filter_gender()
