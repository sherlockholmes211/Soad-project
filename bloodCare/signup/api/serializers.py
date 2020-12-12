from rest_framework import serializers
from signup.models import *

class DonorsDataSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    blood_group = serializers.CharField(max_length=100)
    Age = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=20)
    city    =  serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    address      =  serializers.CharField(max_length=100)

    #hid = serializers.CharField(max_length=16)
    #address = serializers.CharField()
    #adults = serializers.IntegerField()
    #children = serializers.IntegerField()
    #earners = serializers.IntegerField()
    #income = serializers.FloatField()
    #enteredBy = serializers.SlugRelatedField(read_only= True, slug_field='username')

    

    def create(self, validated_data):
        return Donors(**validated_data)

    def update(self, instance, validated_data):
        #user=User.objects.get(user=instance.user)
        instance.blood_group = validated_data.get('blood_group', instance.blood_group)
        #user.city = validated_data.get('city', user.city)
        instance.city = validated_data.get('city', instance.city)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.state = validated_data.get('state', instance.state)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance 

class BloodBankQuerySerializer(serializers.ModelSerializer):
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['city', 'state', 'is_blood_bank', 'is_customer']

class OrderDataSerializer(serializers.Serializer):
    Customer = serializers.CharField(max_length=100)
    Blood_Bank = serializers.CharField(max_length=100)
    blood_type = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    amount = serializers.CharField(max_length=20)
    order_id     =  serializers.CharField(max_length=100)
    #razorpay_payment_id = serializers.CharField(max_length=100)
    paid      =  serializers.CharField(max_length=100)

    #hid = serializers.CharField(max_length=16)
    #address = serializers.CharField()
    #adults = serializers.IntegerField()
    #children = serializers.IntegerField()
    #earners = serializers.IntegerField()
    #income = serializers.FloatField()
    #enteredBy = serializers.SlugRelatedField(read_only= True, slug_field='username')

    

    def create(self, validated_data):
        return order(**validated_data)

    def update(self, instance, validated_data):
        #user=User.objects.get(user=instance.user)
        instance.Customer = validated_data.get('Customer', instance.Customer)
        #user.city = validated_data.get('city', user.city)
        instance.Blood_Bank = validated_data.get('Blood_Bank', instance.Blood_Bank)
        instance.blood_type = validated_data.get('blood_type', instance.blood_type)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.amount = validated_data.get('quantity', instance.quantity)*100
        instance.order_id = validated_data.get('order_id', instance.order_id)
        #instance.razorpay_payment_id = validated_data.get('razorpay_payment_id', instance.razorpay_payment_id)
        instance.paid = validated_data.get('paid', instance.paid)
        instance.save()
        return instance 
