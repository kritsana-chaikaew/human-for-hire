from django.conf.urls import url
from . import views
# import django.contrib.auth.views
from django.contrib.auth import views as auth_views

app_name = 'signupLogin'
urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    # url(r'^login$', views.login, name="login"),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^main$', views.main, name="main"),
    url(r'^logout$', views.logout, name="logout"),
]
