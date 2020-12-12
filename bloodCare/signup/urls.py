from django.urls import path
from . import  views
app_name = 'signup'

urlpatterns=[
     path('customer_register/',views.customer_register, name='customer_register'),
     path('blood_bank_register/',views.blood_bank_register, name='blood_bank_register'),
     path('login/',views.login_view, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('otp_validation/',views.otp_validation,name='otp_validation'),
     path('profile/', views.edit_profile,name='edit-profile'),
     path('bb/view_profile/',views.view_profile,name = 'view-profile'),
     path('bb/edit_profile/',views.bb_edit_profile,name = 'bb-edit-profile'),
     path('blood_request_page/',views.blood_request_page, name='blood_request_page'),
     path('donor_request_page/',views.donor_request_page, name='donor_request_page'),
     path('cart/',views.cart, name='cart'),
     path('success/',views.success, name='success'),
]