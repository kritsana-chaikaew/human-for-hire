from django.conf.urls import url
from . import views

import django.contrib.auth.views

app_name = 'post'
urlpatterns = [
    url(r'^post/$', views.post, name='post'),
    url(r'^post/action/$', views.action, name='action'),
]
