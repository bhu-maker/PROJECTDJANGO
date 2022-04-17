from .import models
from dataclasses import fields
from django import forms
class placeform(forms.ModelForm):
    class Meta:
       model=models.Place
       fields="__all__"

class restaurantform(forms.ModelForm):
    class Meta:
        model=models.Restaurant
        fields="__all__"

class waiterform(forms.ModelForm):
    class Meta:
        model=models.Waiter
        fields="__all__"