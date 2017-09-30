from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import render, redirect

from django.db import IntegrityError
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile
from django.core.files.images import ImageFile

@login_required(login_url='/login')
def main(request):
    return render(request,'main.html',{})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        telephone = request.POST['telephone']
        birthday = request.POST['birthday']
        bankaccount = request.POST['bankaccount']
        profile_image = ImageFile(request.FILES['profile_image'])
        if password != password2:
            return render(request,'signup.html',{'username':username, 'email':email, 'firstname':firstname, 'lastname':lastname, 'address':address, 'telephone':telephone, 'birthday':birthday, "error":"2 passwords is not the same"})
        print(username, password, email, firstname, lastname, address,telephone, birthday)
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
        except (IntegrityError) as e:
            print(str(e))
            if str(e) == "UNIQUE constraint failed: auth_user.username":
                error = "this username has been taken."
            return render(request,'signup.html',{"error": error})
        p = Profile()
        p.user = user
        p.address = address
        p.telephone = telephone
        p.birthday = birthday
        p.bankaccount = bankaccount
        p.image = profile_image
        p.save()
        return redirect('/main')
    return render(request,'signup.html',{})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             return redirect('/main')
#         else:
#             return render(request,'login.html',{'error': 'invalid login'})
#     return render(request,'login.html',{})

def logout(request):
    auth_logout(request)
    return redirect('/login')
