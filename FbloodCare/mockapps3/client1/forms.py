from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.core import validators
from django import forms
from django.db import transaction
from .models import *



class RequestForm(forms.ModelForm):
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    #blood_type = forms.CharField(required=True)
    class Meta():
        model = requestmodel
        fields = ('city','state')

class post_request(forms.ModelForm):
    username = forms.CharField(required=True)
    name = forms.CharField(required=True)
    parental_hospital_name = forms.CharField(required=True)
    category = forms.CharField(required=True)
    License_no = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta():
        model = post_requestmodel1
        fields = ('username','name','parental_hospital_name','category','License_no','phone_number','city','state','address')

class getByIdRequestForm(forms.ModelForm):
    username = forms.CharField(required=True)
    class Meta():
        model = getbyidrequestmodel
        fields = ('username',)