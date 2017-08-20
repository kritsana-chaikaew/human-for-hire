from django.conf.urls import url
from . import views
import django.contrib.auth.views

urlpatterns = [
    url(r'', views.index),
]
