from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import render

def signup(request):
    return render(request,'login.html',{})

def login(request):
    return render(request,'login.html',{})
