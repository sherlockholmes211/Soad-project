from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_blood_bank = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)
    city      =  models.CharField(max_length=100)
    state      =  models.CharField(max_length=100)
    address      =  models.CharField(max_length=100)
    phn_valid    = models.BooleanField(default=0)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    blood_group = models.CharField(max_length=100)
    Age = models.PositiveIntegerField(null=True, blank=True)
    is_donor = models.BooleanField(default=False)
    rewards = models.PositiveIntegerField(default=0,null=True, blank=True)
    def __str__(self):
    	return self.user.username

class Blood_Bank(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    #id_no    = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=100)
    parental_hospital_name = models.CharField(max_length=100)
    category  = models.CharField(max_length=100)
    License_no = models.CharField(max_length=100)
    def __str__(self):
    	return self.user.username

class Blood_storage(models.Model):
    blood_bank = models.OneToOneField(Blood_Bank, on_delete = models.CASCADE,null=True)
    A_p = models.PositiveIntegerField(default =0,null=True, blank=True)
    A_m = models.PositiveIntegerField(default =0,null=True, blank=True)
    B_p = models.PositiveIntegerField(default =0,null=True, blank=True)
    B_m = models.PositiveIntegerField(default =0,null=True, blank=True)
    AB_p = models.PositiveIntegerField(default =0,null=True, blank=True)
    AB_m = models.PositiveIntegerField(default =0,null=True, blank=True)
    O_p = models.PositiveIntegerField(default =0,null=True, blank=True)
    O_m = models.PositiveIntegerField(default =0,null=True, blank=True)
    def __str__(self):
        return str(self.pk)

class order(models.Model):
    Customer = models.CharField(max_length=100)
    Blood_Bank = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    amount = models.CharField(max_length=100 , blank=True)
    order_id = models.CharField(max_length=1000)
    razorpay_payment_id = models.CharField(max_length=1000 ,blank=True)
    paid = models.BooleanField(default=False)



class Validate_otp(models.Model):
    otp = models.IntegerField()
    uid = models.CharField(max_length=12)
    def __str__(self):
        return self.uid



#interested donors.
class Donors(models.Model):
    username = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    Age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    city      =  models.CharField(max_length=100)
    state      =  models.CharField(max_length=100)
    address      =  models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Near_Blood_Banks(models.Model):
    username = models.CharField(max_length=100)
    name      = models.CharField(max_length=100)
    parental_hospital_name = models.CharField(max_length=100)
    category  = models.CharField(max_length=100)
    License_no = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    city      =  models.CharField(max_length=100)
    state      =  models.CharField(max_length=100)
    address      =  models.CharField(max_length=100)
    def __str__(self):
        return self.username

class contact(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    subject = models.TextField(max_length=500)
    message= models.TextField(max_length=500)
    def __str__(self) :
        return self.mail