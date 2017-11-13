from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import render, redirect

from django.db import IntegrityError
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import password_validation as pv

from .models import Profile
from django.core.files.images import ImageFile

from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import datetime
import dateutil
import pytz

# @login_required(login_url='/login')
# def main(request):
#     return render(request,'main.html',{})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        gender = request.POST['gender']
        telephone = request.POST['telephone']
        birthday = request.POST['birthday']
        payment = request.POST['payment']
        profile_image = ImageFile(request.FILES['profile_image'])

        # Check duplicate username
        error = ''
        if User.objects.filter(username=username).exists():
            error = 'This username ( ' + username + ' ) has been taken.'
            return render(request,'signup.html',{'username':username, 'email':email, 'firstname':firstname, 'lastname':lastname, 'address':address, 'telephone':telephone, 'birthday':birthday, 'payment':payment, 'profile_image':profile_image, "error":[error]})

        # Check passwords matching
        error = ''
        if password != password2:
            return render(request,'signup.html',{'username':username, 'email':email, 'firstname':firstname, 'lastname':lastname, 'address':address, 'telephone':telephone, 'birthday':birthday, 'payment':payment, 'profile_image':profile_image, "error":["Passwords dont't match."]})
        else:
            try:
                pv.validate_password(password, request.user)
            except ValidationError as e:
                error = e
                return render(request,'signup.html',{'username':username, 'email':email, 'firstname':firstname, 'lastname':lastname, 'address':address, 'telephone':telephone, 'birthday':birthday, 'payment':payment, 'profile_image':profile_image, "error":error})
            # if (username in password or password in username) or (lastname in password or password in lastname) or (address in password or password in address) or (telephone in password or password in telephone) or (email in password or password in email) or (payment in password or password in payment) or (birthday in password or password in birthday):
            #     error = 'Your password is relating to your personal informations.'
            #     return render(request,'signup.html',{'username':username, 'email':email, 'firstname':firstname, 'lastname':lastname, 'address':address, 'telephone':telephone, 'birthday':birthday, 'payment':payment, 'profile_image':profile_image, "error":[error]})

        # Check Birthday
        bd = datetime.datetime.strptime(birthday, "%Y-%m-%d")
        error = ''
        if bd > datetime.datetime.now():
            error = 'Please check your birthday again'
            return render(request,'signup.html',{'username':username, 'email':email, 'firstname':firstname, 'lastname':lastname, 'address':address, 'telephone':telephone, 'birthday':birthday, 'payment':payment, 'profile_image':profile_image, "error":[error]})

        # If username is unique and passwords are match, then save that username to database.
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        print(username, password, email, firstname, lastname, address,telephone, birthday, payment)

        p = Profile()
        p.user = user
        p.address = address
        p.gender = gender
        p.telephone = telephone
        p.birthday = birthday
        p.payment = payment
        p.image = profile_image
        p.save()
        return redirect('/signup_success')
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

def signup_success(request):
    return render(request,'signup_success.html',{})
