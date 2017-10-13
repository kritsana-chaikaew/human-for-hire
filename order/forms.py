from django import forms
from django.contrib.auth.models import User
from .models import Order
from django.shortcuts import redirect


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ()

    def save(self, commit=True):
        order = super(OrderForm, self).save(commit)
        if commit:
            order.save()
        return order