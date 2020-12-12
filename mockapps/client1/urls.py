
from django.urls import path
from . import views
urlpatterns = [
    path('',views.GetDonorsList,name='get'),
    path('post/',views.PostDonorDetails,name='post'),
    path('username/',views.getDonorbyusername,name='getDonorbyusername'),
    path('update/',views.updatedonor,name='update'),
    path('delete/',views.deletedonor,name='delete')
]
