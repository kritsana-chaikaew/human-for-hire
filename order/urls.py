from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

import django.contrib.auth.views

app_name = 'order'
urlpatterns = [
    url(r'^product/(?P<pk>[0-9]+)/buy/$', views.buy, name='buy'),
    url(r'^manage-work/$', login_required(views.WorkView.as_view()), name='manage_work'),
    url(r'^manage-hired/$', login_required(views.HiredView.as_view()), name='manage_hired'),
    url(r'^ajax/accept_work/$', views.accept_work, name='accept_work'),
    url(r'^ajax/buyer_confirm_workdone/$', views.buyer_confirm_workdone, name='buyer_confirm_workdone'),
    url(r'^ajax/seller_confirm_workdone/$', views.seller_confirm_workdone, name='seller_confirm_workdone'),
    url(r'^ajax/cancel_work/$', views.cancel_work, name='cancel_work'),

    url(r'^rate_employee/(?P<order_no>[0-9]+)/(?P<username>[a-zA-Z0-9_-]+)/$', login_required(views.rate_employee), name='rate_employee'),
    url(r'^rate_employer/(?P<order_no>[0-9]+)/(?P<username>[a-zA-Z0-9_-]+)/$', login_required(views.rate_employer), name='rate_employer'),
]
