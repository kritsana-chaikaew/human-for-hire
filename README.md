### Tools
* git
* heroku CLI
* python
* virtualenv

### Clone Project
```shell
$ git clone https://github.com/kritsana-chaikaew/human-for-hire.git
$ cd human-for-hire/
```

### Checkout New Branch
```shell
$ git checkout -b setup-heroku
```

### Setup Virtual Environment
```shell
$ virtualenv venv
$ source venv/bin/activate
(venv) $
```

### Install Requirements Packages
```shell
(venv) $ vi requirements.txt
```
```text
dj-database-url==0.4.2
Django==1.11.4
gunicorn==19.7.1
psycopg2==2.7.3
whitenoise==3.3.0
```
```shell
(venv) $ pip install -r requirements.txt
```

### Create Simple Hello App
```shell
(venv) $ django-admin startapp hello
(venv) $ vi humanforhire/setting.py
```
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',
]
```
```shell
(venv) $ vi humanforhire/urls.py
```
```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('hello.urls')),
    url(r'', include('hello.urls')),
]
```
```shell
(venv) $ vi hello/urls.py
```
```python
from django.conf.urls import url
from . import views
import django.contrib.auth.views

urlpatterns = [
    url(r'', views.hello),
]
```
```shell
(venv) $ vi hello/view.py
```
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'hello.html',{})
```
```shell
(venv) $ mkdir -p hello/templates
(venv) $ vi hello/hello.html
```
```html
<h1>Hello</h1>
```

### Run Server
```shell
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver
