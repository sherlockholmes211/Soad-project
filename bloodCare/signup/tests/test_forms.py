from django.test import SimpleTestCase,TestCase
from signup.forms import *

class TestForms(TestCase):
    
    # def test_CustomerSignUpForm_valid_data(self):
    #     form = CustomerSignUpForm(data={
    #         'username' : 'sowmya',
    #         'first_name' : 'sowmya',
    #         'last_name' : 'varakala',
    #         'email' : 'sowmya@gmail.com',
    #         'city' : 'miryalguda',
    #         'state' : 'telangana',
    #         'address' : 'gdisnksl',
    #         'phone_number' : '9848429938',
    #         'blood_group' : 'A+',
    #         'Age' : 15,
    #         'password' : 'sowmya@143',
    #         'verify_password' : 'sowmya@143',
    #         'is_donor' : False
    #     })

    #     self.assertTrue(form.is_valid())
    
    # def test_CustomerSignUpForm_no_data(self):
    #     form = CustomerSignUpForm(data ={})

    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors),5)

    def test_EditProfileForm_valid_data(self):
        form = EditProfileForm(data={
            'first_name' : 'sowmya',
            'last_name' : 'varakala',          
            'city' : 'miryalguda',
            'state' : 'telangana',
            'address' : 'gdisnksl',
            'phone_number' : '9848429938'       
        })
        self.assertTrue(form.is_valid())
    
    def test_EditProfileForm_no_data(self):
        form = EditProfileForm(data ={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)



    def test_BloodBankProfileCreationForm_valid_data(self):
        form = BloodBankProfileCreationForm(data={
            'name' : 'sowmya',
            'parental_hospital_name' : 'rainbow',          
            'category' : 'xyz',
            'License_no' : '523'      
        })
        self.assertTrue(form.is_valid())
    
    def test_BloodBankProfileCreationForm_no_data(self):
        form = BloodBankProfileCreationForm(data ={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4) 



    
    def test_BloodStorageProfileCreationForm_valid_data(self):
        form = BloodStorageProfileCreationForm(data={
            'A_p' : 5,
            'A_m' : 5,
            'B_p' : 5,
            'A_m' : 5,
            'AB_p' : 5,
            'AB_m' : 5,
            'O_p' : 0,
            'O_m' : 8
        })
        print(form.errors)
        self.assertTrue(form.is_valid())
     



    def test_BloodBankDetailsQueryForm_valid_data(self):
        form = BloodBankDetailsQueryForm(data={
                     
            'city' : 'miryalguda',
            'state' : 'telangana'       
        })
        self.assertTrue(form.is_valid())
    
    def test_BloodBankDetailsQueryForm_no_data(self):
        form = BloodBankDetailsQueryForm(data ={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)



    def test_contactForm_valid_data(self):
        form = contactForm(data={
            'subject' : 'sowmya',
            'message' : 'rainbow',          
            'name' : 'xyz',
            'mail' : 'sowmya@gmail.com'      
        })
        self.assertTrue(form.is_valid())
    
    def test_contactForm_no_data(self):
        form = contactForm(data ={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)