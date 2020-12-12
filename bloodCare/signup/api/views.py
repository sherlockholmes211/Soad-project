from rest_framework import status
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from signup.models import *
from signup.models import User
from signup.models import Blood_Bank
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from signup.forms import BloodBankDetailsQueryForm
from random import randrange
from django.contrib.auth.decorators import login_required



@api_view(http_method_names=['GET','POST'])
#@permission_classes([IsAuthenticated])
#@login_required(login_url='login')
def donors_list_view(request):
    if request.method == 'GET':
        return donors_list_view_get(request)
    elif request.method == 'POST':
        return donors_list_view_post(request)

def donors_list_view_get(request):
    try:
        city = request.query_params.get('city', None)
        state = request.query_params.get('state', None)
        if city==None:
            data = Donors.objects.filter(state=state)
        elif state==None:
            data = Donors.objects.filter(city=city)
        else:
            data = Donors.objects.filter(city=city,state=state)
        

        serializer = DonorsDataSerializer(data,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def donors_list_view_post(request):
    #enteredBy = request.user
    #hdata = HouseholdData(enteredBy=enteredBy)
    hdata = Donors()
    serializer = DonorsDataSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET','PUT','DELETE'])
#@permission_classes([IsAuthenticated])
def donors_detail_view(request, slug):
    try:
        hdata = Donors.objects.get(username=slug)
        if request.method == 'GET':
            return donors_detail_view_get(request, slug, hdata)
        elif request.method == 'PUT':
            return donors_detail_view_put(request, slug, hdata)
        elif request.method == 'DELETE':
            return donors_detail_view_delete(request, slug, hdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def donors_detail_view_get(request, slug, hdata):
    serializer = DonorsDataSerializer(hdata)
    return Response(serializer.data)

def donors_detail_view_put(request, slug, hdata):
    serializer = DonorsDataSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def donors_detail_view_delete(request, slug, hdata):
    #if request.user==hdata.enteredBy:
    delresult = hdata.delete()
    data = {'message': 'error during deletion'}
    if delresult[0] == 1:
        data = {'message' : 'succesfully deleted'}
    else:
        data = {'message' : 'not same user'}
    return Response(data)

class BloodBankQueryView(generics.GenericAPIView):
    serializer_class = BloodBankQuerySerializer

    def get(self, request):
        city = request.query_params.get('city', None)
        state = request.query_params.get('state', None)
        blood_group = request.query_params.get('blood_group', None)
        self.queryset = User.objects.filter(city=city, state=state)
        serializer = BloodBankQuerySerializer(self.queryset, many=True)
        count = User.objects.filter(city=city, state=state).count()
        blood_banks = []
        blood_bank_names = []
        blood_storages = []
        blood_bank_query_data = {}
        for i in range(count):
            user = User.objects.filter(city=city, state=state)[i]
            try:
                blood_bank = Blood_Bank.objects.get(user=user)
            except ObjectDoesNotExist:
                continue
            blood_banks.append(blood_bank)
            blood_bank_names.append(blood_bank.name)
        for i in range(len(blood_banks)):
            try:
                blood_storage = Blood_storage.objects.get(blood_bank=blood_banks[i])
                if blood_group == 'A+':
                    blood_storages.append(blood_storage.A_p)
                elif blood_group == 'A-':
                    blood_storages.append(blood_storage.A_m)
                elif blood_group == 'B+':
                    blood_storages.append(blood_storage.B_p)
                elif blood_group == 'B-':
                    blood_storages.append(blood_storage.B_m)
                elif blood_group == 'O+':
                    blood_storages.append(blood_storage.O_p)
                elif blood_group == 'O-':
                    blood_storages.append(blood_storage.O_m)
                elif blood_group == 'AB+':
                    blood_storages.append(blood_storage.AB_p)
                elif blood_group == 'AB-':
                    blood_storages.append(blood_storage.AB_m)
            except ObjectDoesNotExist:
                continue
        #blood_bank_query_data['blood_banks'] = blood_bank_names
        #blood_bank_query_data['blood_storages'] = blood_storages
        result =[]
        for i in range(len(blood_bank_names)):
            result.append({"bank_name": blood_bank_names[i],"quatity": blood_storages[i],"blood_group":blood_group})

        return Response(result)

    def post(self, request):
        print("came")

        #Customer = request.user
        #data = order(Customer=Customer)
        #amount= request.quatity * 100
        hdata = order()
        print("came3")
        request.data["amount"]=0
        request.data["order_id"]= randrange(111111,999999)
        request.data["paid"]=0
        serializer = OrderDataSerializer(hdata, data=request.data)
        #print(serializer.Blood_Bank)
        print("came4")
        if serializer.is_valid():
            print("came5")
            serializer.save()
            print("came2")
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, slug):
        hdata = order.objects.get(order_id=slug)
        print(type(hdata.amount))
        request.data["amount"]=hdata.amount
        print(type(hdata.order_id))
        request.data["order_id"]= hdata.order_id
        print(type(hdata.paid))
        request.data["paid"]=str(hdata.paid)
        print("cane3")
        serializer = OrderDataSerializer(hdata, data=request.data)
        print("cane4")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, slug):
        #if request.user==hdata.enteredBy:
        hdata = order.objects.get(order_id=slug)
        delresult = hdata.delete()
        data = {'message': 'error during deletion'}
        if delresult[0] == 1:
            data = {'message' : 'succesfully deleted'}
        else:
            data = {'message' : 'not same user'}
        return Response(data)

"""@api_view(http_method_names=['GET','POST','PUT','DELETE'])
#@permission_classes([IsAuthenticated])
def Hospital(request):
    if request.method == 'PUT':
        return api_update_view(request)
    elif request.method == 'DELETE':
        return api_delete_view(request)

def post(self, request):

        #Customer = request.user
        #data = order(Customer=Customer)
        data = order()
        serializer = OrderDataSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            client = razorpay.Client(auth=('rzp_test_tTJbulofSsAnAO', '1jUvwJJI8cTRmQd3g7HtA2sm'))
            print(client)
            payment = client.order.create({'amount': int(data.amount)*100, 'currency': 'INR','payment_capture': '1'})
            print("payment_order",payment)
            data.order_id = payment['id']
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

def api_update_view(request):

    for i in range(count):
        user = User.objects.filter(city=city, state=state)[i]
        try:
            blood_bank = Blood_Bank.objects.get(user=user)
        except ObjectDoesNotExist:
            continue
        blood_banks.append(blood_bank)
        blood_bank_names.append(blood_bank.name)
    for i in range(len(blood_banks)):
        try:
            blood_storage = Blood_storage.objects.get(blood_bank=blood_banks[i])
            if blood_group == 'A+':
                blood_storages.append(blood_storage.A_p)
            elif blood_group == 'A-':
                blood_storages.append(blood_storage.A_m)
            elif blood_group == 'B+':
                blood_storages.append(blood_storage.B_p)
            elif blood_group == 'B-':
                blood_storages.append(blood_storage.B_m)
            elif blood_group == 'O+':
                blood_storages.append(blood_storage.O_p)
            elif blood_group == 'O-':
                blood_storages.append(blood_storage.O_m)
            elif blood_group == 'AB+':
                blood_storages.append(blood_storage.AB_p)
            elif blood_group == 'AB-':
                blood_storages.append(blood_storage.AB_m)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = BloodBankQuerySerializer(blood_storage,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data = data) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

def api_delete_view(request):

    for i in range(count):
        user = User.objects.filter(city=city, state=state)[i]
        try:
            blood_bank = Blood_Bank.objects.get(user=user)
        except ObjectDoesNotExist:
            continue
        blood_banks.append(blood_bank)
        blood_bank_names.append(blood_bank.name)
    for i in range(len(blood_banks)):
        try:
            blood_storage = Blood_storage.objects.get(blood_bank=blood_banks[i])
            if blood_group == 'A+':
                blood_storages.append(blood_storage.A_p)
            elif blood_group == 'A-':
                blood_storages.append(blood_storage.A_m)
            elif blood_group == 'B+':
                blood_storages.append(blood_storage.B_p)
            elif blood_group == 'B-':
                blood_storages.append(blood_storage.B_m)
            elif blood_group == 'O+':
                blood_storages.append(blood_storage.O_p)
            elif blood_group == 'O-':
                blood_storages.append(blood_storage.O_m)
            elif blood_group == 'AB+':
                blood_storages.append(blood_storage.AB_p)
            elif blood_group == 'AB-':
                blood_storages.append(blood_storage.AB_m)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = blood_storage.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failure"
        
        return Response(data = data)"""