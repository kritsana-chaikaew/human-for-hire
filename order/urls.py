from django.conf.urls import url
from . import views

import django.contrib.auth.views

app_name = 'order'
urlpatterns = [
    url(r'^product/(?P<pk>[0-9]+)/buy/$', views.buy, name='buy'),
    url(r'^manage-work/$', views.manage_work, name='manage_work'),
]
