from django import forms


class BasketAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, label='количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)