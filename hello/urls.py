from django.conf.urls import url
from . import views
import django.contrib.auth.views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^db', views.db),
]
