from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.shortcuts import redirect

# class EditProfileForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = (
#             'first_name',
#             'last_name',
#             'email',
#             'password'
#         )

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit)
        if commit:
            user.save()
        return user