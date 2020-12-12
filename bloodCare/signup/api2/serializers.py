from rest_framework import serializers
from signup.models import *


class BloodBankQuerySerializer(serializers.ModelSerializer):
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    class Meta:
        model = Near_Blood_Banks
        fields = ['username','name','parental_hospital_name','category','License_no','phone_number','city', 'state', 'address']