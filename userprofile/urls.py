from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', login, {'template_name': 'userprofile/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'userprofile/logout.html'}),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password$', views.change_password, name='change_password'),
]