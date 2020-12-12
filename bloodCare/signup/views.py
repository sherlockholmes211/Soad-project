from django.contrib.auth import login, logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage
from .forms import CustomerSignUpForm, BloodBankSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.contrib import messages
from signup import forms
from .models import *
from signup.forms import *
import urllib,json,requests
from random import randrange

#Razorpay
import razorpay
from django.views.decorators.csrf import csrf_exempt
def base(request):
    return render(request,'base.html',{})

def home(request):
    return render(request,'bloodcarehome.html',{})


def gen_otp(uid,phn):
    otp = randrange(111111,999999)
    url = "http://2factor.in/API/V1/89d3d805-c971-11ea-9fa5-0200cd936042/SMS/" + str(phn) +"/"+str(otp)+"/OTPSEND"
    resp = requests.get(url)
    print(resp.json())
    if resp.json().get('Status') == "Success":
        Validate_otp(otp=otp,uid=uid).save()

def customer_register(request):
    registered = False
    if request.method == "POST":
        user_form = CustomerSignUpForm(data = request.POST)
        print("1")
        if user_form.is_valid() :
            print("2")
            user = user_form.save()
            login(request, user)
            #customer=Customer.objects.get(user=user)
            #print(customer.blood_group)
            uid = user.username
            print(uid)
            phn = user.phone_number
            print(phn)
            gt=gen_otp(uid,phn)
            return render(request,'signup/enter_otp.html',{'uid':uid})
            #user.save()
        else:
            return render(request,'signup/customer_register.html',{'user_form_errors':user_form.non_field_errors})
    else:
        user_form = CustomerSignUpForm()
    return render(request,'signup/customer_register.html',{'user_form':user_form,'registered':registered})


"""class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'signup/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')"""
def blood_bank_register(request):
    registered = False
    if request.method == "POST":
        user_form = BloodBankSignUpForm(data = request.POST)

        if user_form.is_valid() :
            user = user_form.save()
            login(request, user)
            #registered=True
            uid = user.username
            print(uid)
            phn = user.phone_number
            print(phn)
            gt=gen_otp(uid,phn)
            return render(request,'signup/enter_otp.html',{'uid':uid})
            #user.save()
        else:
            return render(request,'signup/blood_bank_register.html',{'user_form_errors':user_form.non_field_errors})
    else:
        user_form = BloodBankSignUpForm()
    return render(request,'signup/blood_bank_register.html',{'user_form':user_form,'registered':registered})

"""class blood_bank_register(CreateView):
    model = User
    form_class = BloodBankSignUpForm
    template_name = 'signup/blood_bank_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')"""
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username,password=password)
    

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                #return redirect('signup:register')

            else:
                return HttpResponse("Inactive")
        else:
            return render(request,'signup/invalid.html',{})
    else:
        return render(request,'signup/login.html',{})



""""def login_request(request):
    if request.method=='POST':
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'signup/login.html',
    context={'form':AuthenticationForm()})"""

def logout_view(request):
    logout(request)
    return redirect('/')

# Create your views here.

#OTP



def otp_validation(request):
    validated = False
    registered = False
    invalid = False
    if request.method == "POST":
        otp = request.POST["otp"]
        uid = request.POST["uid"]
        try:
            obj = Validate_otp.objects.get(otp=otp,uid=uid)
            uobj = User.objects.get(username=uid)
            uobj.phn_valid = 1
            uobj.save()
            obj.delete()
            validated = True
            registered=True
            return render(request,'signup/customer_register.html',{'registered':registered,'validated':validated})
        except:
            invalid = True
            obj = Validate_otp.objects.get(uid=uid)
            obj.delete()
            obj1=User.objects.get(username=uid)
            phn = obj1.phone_number
            gt=gen_otp(uid,phn)
            return render(request,'signup/enter_otp.html',{'uid':uid,'invalid':invalid})


# edit profile 
def edit_profile(request):
    print("edit profile ")
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        print("form post ")
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("form is valid")
            print(form)
        return redirect('/')
        
    else:
        form = EditProfileForm(instance =request.user)
        args = {'form':form}

        return render(request, 'profile/profilepage.html',args)
        
#Blood Bank Profile
def view_profile(request):
    bank = Blood_Bank.objects.get(user = request.user)
    blood_storage = Blood_storage.objects.get(blood_bank = bank)
    return render(request,'BBprofile/profilepage.html',{'bank':bank,'blood_storage':blood_storage})

def bb_edit_profile(request):
    blood_bank = Blood_Bank.objects.get(user = request.user)
    blood_storage = Blood_storage.objects.get(blood_bank = blood_bank)
    if request.POST:
        bb_form = BloodBankProfileCreationForm(request.POST,instance = blood_bank)
        bs_form = BloodStorageProfileCreationForm(request.POST,instance = blood_storage)
        if bb_form.is_valid() and bs_form.is_valid():
            profile1 = bb_form.save(commit=False)
            profile2 = bs_form.save(commit=False)
            profile1.save()
            profile2.save()
            return redirect('home')
    else:
        bb_form = BloodBankProfileCreationForm(instance = blood_bank)
        bs_form = BloodStorageProfileCreationForm(instance = blood_storage)
    return render(request, 'BBprofile/profile.html', {'bb_form':bb_form, 'bs_form': bs_form})



    #blood request page and cart and razorpay integration

def blood_request_page(request):
    data = Blood_Bank.objects.all()
    et = []
    
    for t in data:
        et.append({'name' : t.name, 'parental_hospital_name' : t.user.address,'category':t.category,'pk':t.pk,"Storage":"A+={0},A-={1},B+={2},B-={3},AB+={4},AB-={5}".format(t.blood_storage.A_p,t.blood_storage.A_m,t.blood_storage.B_p,t.blood_storage.B_m,t.blood_storage.AB_p,t.blood_storage.AB_m)})
    data = json.dumps(et)
    if request.method =="POST":
        print("In blood request post")
        states = request.POST.get('state')
        cities = request.POST.get('city')
        blood_t = request.POST.get('blood_type')
        data = Blood_Bank.objects.all()
        et = []
        for t in data:
            dic = {"A+":t.blood_storage.A_p,"A-":t.blood_storage.A_m,"B+":t.blood_storage.B_p,"B-":t.blood_storage.B_m,"AB+":t.blood_storage.AB_p,"AB-":t.blood_storage.AB_m,"O+":t.blood_storage.O_p,"O-":t.blood_storage.O_m}
            if t.user.state == str(states) and t.user.city == str(cities) and dic[blood_t]>0:
                print(t.user.state,t.user.city)
                et.append({'name' : t.name, 'parental_hospital_name' : t.user.address,'category':t.category,'pk':t.pk,"Storage":"A+={0},A-={1},B+={2},B-={3},AB+={4},AB-={5}".format(t.blood_storage.A_p,t.blood_storage.A_m,t.blood_storage.B_p,t.blood_storage.B_m,t.blood_storage.AB_p,t.blood_storage.AB_m)})
        data = json.dumps(et)      
    return render(request,'BRP/blood_request_page.html',{"data":data})

def donor_request_page(request):
    data = Customer.objects.all()
    et = []
    
    for t in data:
        et.append({'name' : t.user.username, 'city' : t.user.city,'address':t.user.address,'phone_number':t.user.phone_number,"blood_group":t.blood_group})
    data = json.dumps(et)
    #print(data)
    if request.method =="POST":
        print("In donor request post")

        states = request.POST.get('state')
        cities = request.POST.get('city')
        blood_t = request.POST.get('blood_type')
        data = Customer.objects.all()
        et = []
        for t in data:
            print(t.user.state,t.user.city,t.blood_group,blood_t)
            if t.user.state == str(states) and t.user.city == str(cities) and t.blood_group == str(blood_t):
                
                et.append({'name' : t.user.username, 'city' : t.user.city,'address':t.user.address,'phone_number':t.user.phone_number,"blood_group":t.blood_group})

        data = json.dumps(et)
        return render(request,'BRP/donor_request_page.html',{"data":data})


    return render(request,'BRP/donor_request_page.html',{"data":data})
    
#razorpay integration
def cart(request):
    if request.method == "POST":
        print("In cart request post")

        if request.POST.get("form_type") == 'formOne':
            k = request.POST.get('pk')
            userobjects = request.user
            print(userobjects)
            print("User city",userobjects.customer.rewards)
            data = Blood_Bank.objects.get(pk=k)
            print("formOne")
            return render(request,'BRP/cart.html',{"Blood_Bank":data,"user":userobjects})

        if request.POST.get("form_type") == 'formTwo':
            print("formTwo")
            username = request.user
            print(username)

            amount = request.POST.get('amount')
            BB_name = request.POST.get('Blood_Bank_name')
            blood_t = request.POST.get('blood_type')
            print(blood_t)

            print("BB_name",BB_name)

            print(amount)
            #amount = amount*100 converting units into ruppes
            client = razorpay.Client(auth=('rzp_test_tTJbulofSsAnAO', '1jUvwJJI8cTRmQd3g7HtA2sm'))
            print(client)
            payment = client.order.create({'amount': int(amount)*100, 'currency': 'INR','payment_capture': '1'})
            print("payment_order",payment)
            order1 = order(Customer=username,quantity=2,amount=amount,order_id=payment['id'],Blood_Bank=BB_name,blood_type=blood_t)
            print(order1)
            order1.save()
            return render(request,'BRP/cart.html',{"pid":payment['id'],"payment":True})
    else:
        return render(request,'BRP/cart.html',{"payment":False})
@csrf_exempt
def success(request):
    if request.method == "POST":
        a =  (request.POST)
        order_id = ""
        for key , val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break

        user = order.objects.filter(order_id = order_id).first()
        user.paid = True
        user.save()
    return render(request, "BRP/success.html")


def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=True)
            save_it.save()
            return render(request,'contact/thanks.html')
    else:
        form = FeedbackForm()
    return render(request,'contact/form.html',{'form': form})
