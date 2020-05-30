from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'city']


class OrderCreateAnonForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone', 'first_name', 'address', 'city']
