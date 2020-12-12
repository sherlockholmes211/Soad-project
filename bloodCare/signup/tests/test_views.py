from django.test import TestCase,Client
from django.urls import reverse
from signup.models import User,Customer,Blood_Bank,Blood_storage,order,Validate_otp,Donors,Near_Blood_Banks,contact
import json


class TestViews(TestCase):
  
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('donors_list_view')
        self.detail_url = reverse('donors_detail_view',args=['siva'])
        self.bloodbank_url = reverse('blood-bank')
        self.user = User.objects.create(
            is_customer  = False,
            is_blood_bank =False,
            phone_number = '9177026646',
            city = 'vjd',
            state  = 'andhra',
            address = 'uadhfa',
            phn_valid = 0


        )
        self.user.save()
        self.customer_post_data ={
           "username": "siva",
           "blood_group": "o+",
           "Age": 23,
           "phone_number": "9177036646",
           "city": "vjd",
           "state": "andhra",
           "address": "abcde"
        }
        self.donor_post_data = {
            "Customer" : "siva",
            "Blood_Bank" : "bloodorg",
            "blood_type" : "o+",
            "quantity" : 5,
            "amount" : "fghwt",
            "order_id" : 111120,
            "razorpay_payment_id" : "adf",
            "paid" : True
        }

        self.near_bloodbank_url = reverse('blood-bank1')
        self.near_blood_bank = Near_Blood_Banks.objects.create(
            username  = "banker11",
            name ="banker11",
            parental_hospital_name = '9177026646',
            category = "government",
            License_no = "123456",
            phone_number = "123456789",
            city = 'vjd',
            state  = 'ap',
            address = 'uadhfa',
        )
        self.near_blood_bank.save()
        self.near_blood_bank_post_data ={
            "username"  : "banker11",
            "name" :"banker11",
            "parental_hospital_name" : '9177026646',
            "category" : "government",
            "License_no" : "123456",
            "phone_number" : "123456789",
            "city" : 'vjd',
            "state"  : 'ap',
            "address" : 'uadhfa',
         }


  
  
    def test_donors_list_view_get(self):
        
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code,200)
        #self.assertTemplateUsed(response, '')

    def test_donors_list_view_post(self):
        
        response = self.client.post(self.list_url, self.customer_post_data)

        self.assertEqual(response.status_code,200)


    def test_donors_detail_view_get(self):
        self.client.post(self.list_url, self.customer_post_data)
        response = self.client.get(self.detail_url)
        
        self.assertEqual(response.status_code,200)
       #self.assertTemplateUsed(response, '')


    def test_donors_detail_view_post(self):
        
        response = self.client.post(self.detail_url, self.customer_post_data)

        self.assertEqual(response.status_code,405)

    def test_get(self):
        
        response = self.client.get(self.bloodbank_url)

        self.assertEqual(response.status_code,200)

    # def test_post(self):
        
    #     response = self.client.post(self.bloodbank_url, self.donor_post_data)

    #     self.assertEqual(response.status_code,200)


    
    def test_near_bloodbank_list_view_get(self):
        
        response = self.client.get(self.near_bloodbank_url)

        self.assertEqual(response.status_code,200)
        #self.assertTemplateUsed(response, '')

    def test__near_bloodbank_list_view_post(self):

        response = self.client.post(self.near_bloodbank_url, self.near_blood_bank_post_data)

        self.assertEqual(response.status_code,201)