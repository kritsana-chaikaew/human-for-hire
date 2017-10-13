from django.conf.urls import url
from . import views

import django.contrib.auth.views

app_name = 'order'
urlpatterns = [
    url(r'^buy/$', views.buy, name='buy'),
]
