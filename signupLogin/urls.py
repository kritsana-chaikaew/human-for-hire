from django.conf.urls import url
from . import views
import django.contrib.auth.views

app_name = 'post'
urlpatterns = [
    url(r'^signup/$', views.signup),
    url(r'^login$', views.login),
]
