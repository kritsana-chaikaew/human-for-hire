# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from hello.models import Person
# Create your views here.
def hello(request):
    return render(request,'hello.html',{})

def db(request):
    person = Person()
    person_info = Person.objects.all()

    return render(request, 'db.html', {'person_info': person_info})
