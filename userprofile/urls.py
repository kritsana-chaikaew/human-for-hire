from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

app_name = 'userprofile'
urlpatterns = [
    url(r'^logout/$', logout, {'template_name': 'userprofile/logout.html'}),
    url(r'^$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password$', views.change_password, name='change_password'),
]
