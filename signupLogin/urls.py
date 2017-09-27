from django.conf.urls import url
from . import views
import django.contrib.auth.views

app_name = 'signupLogin'
urlpatterns = [
    url(r'^signup/$', views.signup),
    url(r'^login$', views.login),
    url(r'^main$', views.main),
    url(r'^logout$', views.logout, name="logout"),
]
