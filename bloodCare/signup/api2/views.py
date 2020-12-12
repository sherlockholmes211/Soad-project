from rest_framework import status
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from signup.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from signup.forms import BloodBankDetailsQueryForm



class BloodBankQueryView(generics.GenericAPIView):
    serializer_class = BloodBankQuerySerializer
    queryset = Near_Blood_Banks.objects.all()
    def get(self, request):
        try:
            city = request.query_params.get('city', None)
            state = request.query_params.get('state', None)
            data = Near_Blood_Banks.objects.filter(city=city,state=state)
            serializer = BloodBankQuerySerializer(data,many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        serializer = BloodBankQuerySerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print("is valid")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Blood_bank_DetailAPIView(generics.GenericAPIView):    
    queryset = Near_Blood_Banks.objects.all()
    serializer_class = BloodBankQuerySerializer
    def put(self, request, slug):
        print("username",slug)
        article = Near_Blood_Banks.objects.get(username=slug)
        if article is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = BloodBankQuerySerializer(article, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        article = Near_Blood_Banks.objects.get(username=slug)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""def household_list_view_post(request):
    enteredBy = request.user
    hdata = HouseholdData(enteredBy=enteredBy)
    serializer = HouseholdDataSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def household_detail_view(request, slug):
    try:
        hdata = HouseholdData.objects.get(hid=slug)
        if request.method == 'GET':
            return household_detail_view_get(request, slug, hdata)
        elif request.method == 'PUT':
            return household_detail_view_put(request, slug, hdata)
        elif request.method == 'DELETE':
            return household_detail_view_delete(request, slug, hdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def household_detail_view_get(request, slug, hdata):
    serializer = HouseholdDataSerializer(hdata)
    return Response(serializer.data)

def household_detail_view_put(request, slug, hdata):
    serializer = HouseholdDataSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def household_detail_view_delete(request, slug, hdata):
    if request.user==hdata.enteredBy:
        delresult = hdata.delete()
        data = {'message': 'error during deletion'}
        if delresult[0] == 1:
            data = {'message' : 'succesfully deleted'}
    else:
        data = {'message' : 'not same user'}
    return Response(data)"""
    

"""
@api_view(http_method_names=['GET','POST',])
#@permission_classes([IsAuthenticated])
def banks_list_view(request):
    if request.method == 'GET':
        return banks_list_view_get(request)
    #elif request.method == 'POST':
     #   return household_list_view_post(request)

def banks_list_view_get(request):
    try:
        city = request.query_params.get('city', None)
        state = request.query_params.get('state', None)
        data = Near_Blood_Banks.objects.filter(city=city,state=state)
        

        serializer = BanksDataSerializer(data,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

"""