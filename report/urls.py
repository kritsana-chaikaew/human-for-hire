from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'report'
urlpatterns = [
    url(r'^report/$', views.create_report, name="create_report"),
    url(r'^report_success$', views.report_success, name="report_success"),
]
