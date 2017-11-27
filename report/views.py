from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import Report
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def create_report(request):
    if request.method == 'POST':
        r = Report()
        r.user = User.objects.get(id=request.user.id)
        r.subject = request.POST['report_subject']
        r.description = request.POST['report_description']
        r.save()
        return render(request, 'report/report_success.html',{})
    return render(request, 'report/report.html',{})

def report_success(request):
    return render(request,'report/report_success.html',{})

        
