from django.conf.urls import url
from . import views
import django.contrib.auth.views

app_name = 'hello'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
