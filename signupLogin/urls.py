from django.conf.urls import url
from . import views
import django.contrib.auth.views

app_name = 'signupLogin'
urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login$', views.login, name="login"),
    url(r'^main$', views.main, name="main"),
    url(r'^logout$', views.logout, name="logout"),
]
