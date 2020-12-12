from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
from .forms import *
# Create your views here.


def GetstorageList(request):
    form = RequestForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            blood_group = form.cleaned_data['blood_group']

            print("one")
            r = requests.get(' http://127.0.0.1:8000/api/blood-bank?city=' + city + '&state='+ state +'&blood_group='+ blood_group)
            data = r.json()
            print("onee")
            return render(request,'results.html',{'data' : data,'city':city,'state':state, 'blood_group':blood_group})
    else:
        return render(request,'request.html')


def PlaceOrder(request):
    form = post_request(request.POST)
    if request.method=="POST":
        if form.is_valid():
            r = requests.post('http://127.0.0.1:8000/api/blood-bank/',data = request.POST)
            data = r.json()
            print(data)
            return render(request,'results2.html',{'data' : data, 'msg':"ORDER PLACED !!!"})
    else:
        return render(request,'post_request.html',{'form' : form})


def getDonorbyusername(request):
    form = getByIdRequestForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            id = form.cleaned_data['username']
            r = requests.get('http://127.0.0.1:8000/api/donors/'+id)
            donor = r.json()
            data = []
            data.append(donor)
            return render(request,'results.html',{'data' : data})
    else:
        return render(request,'getbyid.html',{'form' : form})

def updatedonor(request):
    form = post_request(request.POST)
    if request.method=="POST":
        if form.is_valid():
            id = form.cleaned_data['username']
            r = requests.put('http://127.0.0.1:8000/api/donors/'+id,data = request.POST)
            donor = r.json()
            data = []
            data.append(donor)
            return render(request,'results.html',{'data' : data})
    else:
        return render(request,'update.html',{'form' : form})

def deletedonor(request):
    form = getByIdRequestForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            id = form.cleaned_data['username']
            r = requests.delete('http://127.0.0.1:8000/api/donors/'+id)
            return HttpResponse('Deleted Successfully')
    else:
        return render(request,'update.html',{'form' : form})



    


