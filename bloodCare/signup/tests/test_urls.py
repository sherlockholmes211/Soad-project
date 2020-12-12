from django.test import SimpleTestCase
from django.urls import reverse, resolve
from signup.views import *
from signup.api.views import *
from signup.api2.views import *
from rest_framework.test import APITestCase

class TestUrls(SimpleTestCase):

    def test_customer_register_url_is_resolved(self):
        url = reverse('signup:customer_register')
        found = resolve(url)
        self.assertEquals(found.func, customer_register)

    def test_bloodbank_register_url_is_resolves(self):
        url = reverse('signup:blood_bank_register')
        self.assertEquals(resolve(url).func, blood_bank_register)

    def test_login_is_resolves(self):
        url = reverse('signup:login')
        self.assertEquals(resolve(url).func, login_view)

    def test_logout_is_resolves(self):
        url = reverse('signup:logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_otp_validation_is_resolves(self):
        url = reverse('signup:otp_validation')
        self.assertEquals(resolve(url).func, otp_validation)
    
    def test_edit_profile_is_resolves(self):
        url = reverse('signup:edit-profile')
        self.assertEquals(resolve(url).func, edit_profile)
    
    def test_view_profile_is_resolves(self):
        url = reverse('signup:view-profile')
        self.assertEquals(resolve(url).func, view_profile)
    
    def test_bb_edit_profile_is_resolves(self):
        url = reverse('signup:bb-edit-profile')
        self.assertEquals(resolve(url).func, bb_edit_profile)
    
    def test_blood_request_page_is_resolves(self):
        url = reverse('signup:blood_request_page')
        self.assertEquals(resolve(url).func, blood_request_page)
    
    def test_donor_request_page_is_resolves(self):
        url = reverse('signup:donor_request_page')
        self.assertEquals(resolve(url).func, donor_request_page)
    
    def test_cart_is_resolves(self):
        url = reverse('signup:cart')
        self.assertEquals(resolve(url).func, cart)
    
    def test_success_is_resolves(self):
        url = reverse('signup:success')
        self.assertEquals(resolve(url).func, success)
    

class TestAPIUrls(APITestCase):

    def test_donors_list_url_is_resolved(self):
        path = reverse('donors_list_view')
        found = resolve(path)
        self.assertEquals(found.func.__name__,donors_list_view.__name__)
   
    def test_donors_detail_url_is_resolved(self):
        path = reverse('donors_detail_view', args = ['some-slug'])
        found = resolve(path)
        self.assertEquals(found.func.__name__,donors_detail_view.__name__)
    
    def test_BloodBankQueryView_is_resolved(self):
        path = reverse('blood-bank')
        found = resolve(path)
        self.assertEquals(found.func.__name__,BloodBankQueryView.__name__)
   
    def test_BloodBankQueryView_is_resolved(self):
        path = reverse('blood-bank',args = ['some-slug'])
        found = resolve(path)
        self.assertEquals(found.func.__name__,BloodBankQueryView.__name__)

    def test_banks_list_view_is_resolved(self):
        path = reverse('blood-bank1')
        found = resolve(path)
        self.assertEquals(found.func.__name__,BloodBankQueryView.__name__)
    
    # def test_api_token_auth_is_resolved(self):
    #     path = reverse('api_token_auth')
    #     found = resolve(path)
    #     self.assertEquals(found.func._name,obtain_auth_token.name_)