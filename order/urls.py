from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

import django.contrib.auth.views

app_name = 'order'
urlpatterns = [
    url(r'^product/(?P<pk>[0-9]+)/buy/$', views.buy, name='buy'),
    url(r'^manage-work/$', login_required(views.WorkView.as_view()), name='manage_work'),
    url(r'^ajax/accept_work/$', views.accept_work, name='accept_work'),
]
