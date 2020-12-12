
from django.urls import path
from . import views
urlpatterns = [
    path('',views.GetstorageList,name='get'),
    path('post/',views.PlaceOrder,name='post'),
    path('username/',views.getDonorbyusername,name='getDonorbyusername'),
    path('update/',views.updatedonor,name='update'),
    path('delete/',views.deletedonor,name='delete')
]
