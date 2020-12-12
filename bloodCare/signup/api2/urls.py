from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('blood-bank/', views.BloodBankQueryView.as_view(), name="blood-bank1"),
    #path('householddata/<slug:slug>',views.household_detail_view, name="household_detail_view"),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
    path('blood-bank/<slug:slug>/', views.Blood_bank_DetailAPIView.as_view()), 
]