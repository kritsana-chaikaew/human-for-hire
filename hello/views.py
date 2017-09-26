# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from hello.models import Person
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
	model = Person
	template_name = 'hello/index.html'


def db(request):
    person = Person()
    person_info = Person.objects.all()

    return render(request, 'db.html', {'person_info': person_info})
