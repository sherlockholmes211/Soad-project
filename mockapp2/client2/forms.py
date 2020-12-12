from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.core import validators
from django import forms
from django.db import transaction
from .models import *

class RequestForm(forms.ModelForm):
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    blood_group=forms.CharField(required=True)
    class Meta():
        model = requestmodel
        fields = ('city','state','blood_group')

class post_request(forms.ModelForm):
    Customer = forms.CharField(required=True)
    Blood_Bank = forms.CharField(required=True)
    blood_type = forms.CharField(required=True)
    quantity = forms.IntegerField(required=True)

    class Meta():
        model = post_requestmodel
        fields = ('Customer','Blood_Bank','blood_type','quantity')

class getByIdRequestForm(forms.ModelForm):
    username = forms.CharField(required=True)
    class Meta():
        model = getbyidrequestmodel
        fields = ('username',)