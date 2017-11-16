from django.conf.urls import url

from . import views
import django.contrib.auth.views

app_name = 'hello'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^product/(?P<pk>[0-9]+)/$',
        views.ProductDetailView.as_view(),
        name='product-detail'),
    url(r'^tags/(?P<tags>.+)/$',
        views.TagResultView.as_view(),
        name='tag-result'),
    url(r'^get_tags/',
        views.get_tags,
        name='get_tags'),
]
