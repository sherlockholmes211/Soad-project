from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('donors',views.donors_list_view, name="donors_list_view"),
    path('donors/<slug:slug>',views.donors_detail_view, name="donors_detail_view"),
    path('blood-bank/', views.BloodBankQueryView.as_view(), name="blood-bank"),
    path('blood-bank/<slug:slug>', views.BloodBankQueryView.as_view(), name="blood-bank"),
    #path('blood-bank2/',views.Hospital , name="Hospital"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),    
]