from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from userprofile.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, 'userprofile/home.html')


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'userprofile/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/userprofile/profile')
        
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'userprofile/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/userprofile/profile')
        else:
            return redirect('/userprofile/change-password')
    
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'userprofile/change_password.html', args)
        