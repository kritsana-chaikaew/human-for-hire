from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'signuplogin'
urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', auth_views.login, {'template_name': 'signuplogin/login.html'}, name='login'),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^signup_success$', views.signup_success, name="signup_success"),
]
