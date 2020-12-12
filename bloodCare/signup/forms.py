from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.core import validators
from django import forms
from django.db import transaction
from .models import *


class CustomerSignUpForm(forms.ModelForm):
    blood_group = forms.CharField(required=True)
    Age = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())
    verify_password = forms.CharField(widget=forms.PasswordInput())
    is_donor =   forms.BooleanField(required=False)

    def clean(self):
        password = self.cleaned_data['password']
        verify_password = self.cleaned_data['verify_password']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("User already exists")
        if password!=verify_password :
            raise forms.ValidationError("Password Donot Match")
        if len(first_name) == 0:
            raise forms.ValidationError("Invalid first_name")
        if len(last_name) == 0:
            raise forms.ValidationError("Invalid last_name")


    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password','verify_password','blood_group','Age','city','state','address','phone_number','is_donor')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.set_password(user.password)
        user.save()
        customer = Customer.objects.create(user=user)
        customer.is_donor = self.cleaned_data.get('is_donor')
        customer.blood_group=self.cleaned_data.get('blood_group')
        customer.Age =self.cleaned_data.get('Age')
        customer.city=self.cleaned_data.get('city')
        customer.state=self.cleaned_data.get('state')
        customer.address=self.cleaned_data.get('address')
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.save()
        if(customer.is_donor==True):
            donors = Donors.objects.create(username=user.username,blood_group=customer.blood_group,Age=customer.Age,phone_number=customer.phone_number,city=customer.city,state =customer.state,address=customer.address)
            donors.save()
        return user

class BloodBankSignUpForm(forms.ModelForm):
    name      = forms.CharField(max_length=100)
    parental_hospital_name = forms.CharField(max_length=100)
    category  = forms.CharField(max_length=100)
    License_no = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    verify_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        password = self.cleaned_data['password']
        verify_password = self.cleaned_data['verify_password']
        name = self.cleaned_data['name']
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("User already exists")
        if password!=verify_password :
            raise forms.ValidationError("Password Donot Match")
        if len(name) == 0:
            raise forms.ValidationError("Invalid name")
    

    class Meta():
        model = User
        fields = ('username','name','email','password','verify_password','parental_hospital_name','category','License_no','city','state','address','phone_number')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_blood_bank = True
        user.set_password(user.password)
        user.is_staff = True
        user.email    = self.cleaned_data.get('email')
        user.save()
        bank = Blood_Bank.objects.create(user=user)
        bank.name=self.cleaned_data.get('name')
        bank.parental_hospital_name=self.cleaned_data.get('parental_hospital_name')
        bank.category=self.cleaned_data.get('category')
        bank.License_no=self.cleaned_data.get('License_no')
        bank.city=self.cleaned_data.get('city')
        bank.state=self.cleaned_data.get('state')
        bank.address=self.cleaned_data.get('address')
        bank.phone_number=self.cleaned_data.get('phone_number')
        bank.save()
        storage = Blood_storage.objects.create(blood_bank=bank)
        storage.save()
        banks = Near_Blood_Banks.objects.create(username=user.username,name=bank.name,parental_hospital_name=bank.parental_hospital_name,category=bank.category,phone_number=bank.phone_number,city=bank.city,state =bank.state,License_no=bank.License_no,address=bank.address)
        banks.save()
        return user

class EditProfileForm(UserChangeForm):
    class Meta():
        model= User
        fields=['first_name','last_name','phone_number','city','state','address']

class BloodBankProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Blood_Bank
        fields = [
                 'name',  
                 'parental_hospital_name',
                 'category',
                 'License_no',
        ]



class BloodStorageProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Blood_storage
        fields = [
                #  'blood_bank'
                 'A_p',
                 'A_m',
                 'B_p',
                 'B_m',
                 'AB_p',
                 'AB_m',
                 'O_p',
                 'O_m',
        ]

class BloodBankDetailsQueryForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'city',
            'state',
        ]

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['subject','message','name','mail']