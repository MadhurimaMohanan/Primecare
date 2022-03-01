from django.shortcuts import render
import ast
from .models import P_user
# from .models import P_details
from .models import P_Photo
from .models import P_previous_employer

from .models import P_Work_permit_certificate
from .models import P_Address
from .models import P_Insurance
from .models import P_Sssc
from .models import P_Pvg

from .models import P_Experience
from .models import P_Contact
from .models import user_temp
from .models import P_caretaker
from .models import P_CV
from .models import P_admin
# from .models import P_Staff_details

from django.views import View
from django.core.files.base import ContentFile

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import userSerializer
from .serializers import contactSerializer

from django.http import JsonResponse
from .forms import ContactModelForm

from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import random

from django.contrib.auth.hashers import make_password,check_password
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index(request):
    return render(request,'index1.html')



    
def staff_register(request):
    try:
        del request.session['userid']
    except:
        pass
    try:
        del request.session['tempid']
    except:
        pass
    return render(request,'staff_registration.html')

class Staff_reg_func(View):
    def post(self, request):
        # select=request.POST.get('select', None)
        Firstname=request.POST.get('Firstname', None)
        Lastname=request.POST.get('Lastname', None)
        dob=request.POST.get('dob', None)
        PhoneNumber=request.POST.get('PhoneNumber', None)
        Email=request.POST.get('Email', None)
        Password=request.POST.get('Password', None)
        address1=request.POST.get('address1', None)
        address2=request.POST.get('address2', None)
        address3=request.POST.get('address3', None)
        postcode=request.POST.get('postcode', None)
        
        check=P_user.objects.filter(Email=Email)
        if check:
            mytemp=user_temp()
            # mytemp.select=select
            mytemp.Firstname=Firstname
            mytemp.Lastname=Lastname
            mytemp.Date_of_birth=dob
            mytemp.PhoneNumber=PhoneNumber
            mytemp.Email=Email
            mytemp.Password=make_password(Password)
            mytemp.Address_1=address1
            mytemp.Address_2=address2
            mytemp.Address_3=address3
            mytemp.postcode=postcode
            mytemp.save()
            request.session['tempid']=mytemp.id
            for i in range(100):
                otp = random.randint(100000, 999999)
            mytemp.otp=otp
            mytemp.save()
            subject = 'Your accounts need to be verified'
            message = f'Hii {mytemp.Firstname} this is your otp {mytemp.otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list=[mytemp.Email]
            send_mail(subject, message ,email_from,recipient_list)

            my_data = {
                "id_session": request.session['tempid'],
                "temp_id": mytemp.id
            }
            return render(request,'otp.html',{'data': my_data})

        else:
            myuser=P_user()
            # myuser.select=select
            myuser.Firstname=Firstname
            myuser.Lastname=Lastname
            myuser.Date_of_birth=dob
            myuser.PhoneNumber=PhoneNumber
            myuser.Email=Email
            myuser.Password=make_password(Password)
            myuser.Address_1=address1
            myuser.Address_2=address2
            myuser.Address_3=address3
            myuser.postcode=postcode

            myuser.save()
            request.session['userid']=myuser.id

            for i in range(100):
                otp = random.randint(100000, 999999)
            myuser.otp=otp
            myuser.save()
            subject = 'Your accounts need to be verified'
            message = f'Hii {myuser.Firstname} this is your otp {myuser.otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list=[myuser.Email]
            send_mail(subject, message ,email_from,recipient_list)

            my_data = {
                "id_session": request.session['userid'],
                "user_id": myuser.id
            }
            
            return render(request,'otp.html', {'data': my_data})





class userList(APIView):

    def get(self,request):
        user1=P_user.objects.all()
        serializer=userSerializer(user1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

#
class contact(View):
    def post(self,request):
        contact = P_Contact(Name=request.POST['name'], Subject=request.POST['subject'], Email=request.POST['email'], Message=request.POST['message'])
        contact.save()
        return HttpResponseRedirect('/')
        

       
        
        
 


class contactList(APIView):

    def get(self,request):
        contact1=P_Contact.objects.all()
        serializer=contactSerializer(contact1,many=True)
        return Response(serializer.data)

class otp_cnfrm(View):
    def post(self,request):
        otp=request.POST['otp']

        # temp condition
        try:
            tid=request.session['tempid']
            check1=user_temp.objects.filter(id=tid, otp=otp)
            print('madhurima')
            if check1.exists():
                my_tmp_user = check1[0]
                myusers=P_user.objects.filter(Email=my_tmp_user.Email)
                myuser=myusers[0]
                # P_user.objects.filter(Email=user_temp.Email).update(otp=otp)
                myuser.Firstname=my_tmp_user.Firstname
                myuser.Lastname=my_tmp_user.Lastname
                myuser.PhoneNumber=my_tmp_user.PhoneNumber
                myuser.Date_of_birth=my_tmp_user.Date_of_birth
                myuser.Email=my_tmp_user.Email
                myuser.Password=my_tmp_user.Password
                myuser.Address_1=my_tmp_user.Address_1
                myuser.Address_2=my_tmp_user.Address_2
                myuser.Address_3=my_tmp_user.Address_3
                myuser.postcode=my_tmp_user.postcode
                myuser.otp=my_tmp_user.otp
                myuser.save()
                my_tmp_user.delete()
                request.session['userid']=myuser.id
                return render(request,'staff_upload.html')
            else:
                return render(request,'otp.html',{'msg':'OTP is Invalid'})
        except KeyError:
            mid=request.session['userid']
            check3=P_user.objects.filter(id=mid, otp=otp)
            if check3.exists():
                return render(request,'staff_upload.html')
            else:
                return render(request,'otp.html',{'msg':'OTP is Invalid'})

            

class file_upload(View):
    def post(self,request):
        # otp=request.POST['otp']
        mid=request.session['userid']
        SortCode=request.POST['SortCode']
        Photo=request.FILES['Photo']
        # Covidteststatus=request.POST['Covidteststatus']
        # Covid_test_expire_date=request.POST['Covid_test_expire_date']
        # Certificate=request.FILES['Certificate']
        vaccine1=request.POST['vaccine1']
        vaccine2=request.POST['vaccine2']
        booster=request.POST['booster']
        passport=request.FILES['passport']
        visa=request.FILES['visa']
        brp=request.FILES['brp']
        passport_expiry_date=request.POST['passport_expiry_date']
        visa_expiry_date=request.POST['visa_expiry_date']
        brp_expiry_date=request.POST['visa_expiry_date']
        
        employername1=request.POST['employername1']
        telenum1=request.POST['telenum1']
        employermail1=request.POST['employermail1']
        address1=request.POST['address1']
        employername2=request.POST['employername2']
        telenum2=request.POST['telenum2']
        employermail2=request.POST['employermail2']
        address2=request.POST['address2']
        try: 
            payslip1=request.FILES['payslip1']
            payslip2=request.FILES['payslip2']
        except:
            payslip1=False
            payslip2=False    
       
        Proof=request.FILES['Proof']
        # Insurance=request.FILES['Insurance']
        # expiry_date=request.POST['expiry_date']
        certificate=request.FILES['certificate']
        expiry_date=request.POST['expiry_date1']
        skills=request.POST['skills']
        cv=request.FILES['Cv']
        try:
            pvg=request.FILES['pvg']
        except:
            pvg=False
        pvgnum=request.POST['pvgnum']
        manual=request.FILES['manual']
        firesafety=request.FILES['firesafety']
        health=request.FILES['health']
        # expiry_date=request.POST['expiry_date']
        infection=request.FILES['infection']
        accno=request.POST['AccNo']
        ni=request.POST['ni']
        status=request.POST['status']
        # toc=request.POST['toc']
        check=P_user.objects.get(id=mid)
        if check:
            myphoto=P_Photo()
            myphoto.Photo=Photo
            myphoto.save()
            mycv=P_CV()
            mycv.cv=cv
            mycv.save()

            mypermit=P_Work_permit_certificate()
            mypermit.passport=passport
            mypermit.visa=visa
            mypermit.brp=brp
            mypermit.passport_expiry_date=passport_expiry_date
            mypermit.visa_expiry_date=visa_expiry_date
            mypermit.brp_expiry_date=brp_expiry_date
            mypermit.save()

            myemployer=P_previous_employer()
            
            myemployer.employername1=employername1
            myemployer.telenum1=telenum1
            myemployer.employermail1=employermail1
            myemployer.address1=address1
            myemployer.employername2=employername2
            myemployer.telenum2=telenum2
            myemployer.employermail2=employermail2
            myemployer.address2=address2
            
            myemployer.payslip1=payslip1
            myemployer.payslip2=payslip2
            myemployer.save()
            myaddress=P_Address()
            myaddress.Proof= Proof
            myaddress.save()
            # myinsurance=P_Insurance()
            # myinsurance.Insurance= Insurance
            # myinsurance.expiry_date=expiry_date
            # myinsurance.save()
            mysssc=P_Sssc()
            mysssc.certificate=certificate
            mysssc.expiry_date=expiry_date
            mysssc.save()
            mypvg=P_Pvg()
            mypvg.pvg=pvg
            mypvg.pvgno=pvgnum
            mypvg.save()
            myexperience=P_Experience()
            myexperience.ManualHandling=manual
            myexperience.FireSafety=firesafety
            myexperience.HealthSafety=health
            myexperience.InfectionControl=infection
            myexperience.save()
          

            myuser=P_user.objects.get(id=mid)
            print(myuser)
            myuser.SortCode=SortCode
            myuser.skills=skills
            myuser.Cv_id=mycv
            myuser.Photo_id=myphoto
            myuser.Previous_id=myemployer
            myuser.vaccine1=vaccine1
            myuser.vaccine2=vaccine2
            myuser.booster=booster
            # myuser.Covidteststatus=Covidteststatus
            # myuser.Covid_test_expire_date=Covid_test_expire_date
            myuser.Sssc_id=mysssc
            myuser.workpermit_id=mypermit
            # myuser.Insurance_id=myinsurance
            myuser.Address_id=myaddress
            myuser.Pvg_id=mypvg
            # myuser.Qualification_id= myqualification
            # myuser.Handbook_id= myhandbook
            # myuser.Contract_id= mycontract
            myuser.Experience_id= myexperience
            myuser.AccountNo=accno
            myuser.NInumber=ni
            myuser.status=status
            # myuser.toc= toc
            myuser.save()
            return render(request,'success.html')
        else:
            return render(request,'failed.html')

class care_reg(View):
    def get(self,request):
        return render(request,'caretaker_reg.html')

class care_reg_func(View):
    def post(self,request):
        name=request.POST['name']
        email=request.POST['email']
        phonenumber=request.POST['Phonenumber']
        description=request.POST['description']
        check=P_caretaker.objects.filter(email=email)
        if check:
            return render(request,'caretaker_reg.html',{'msg':'Email already exists'})
        else:
            mycare=P_caretaker()
            mycare.name=name
            mycare.email=email
            mycare.phonenumber=phonenumber
            mycare.description=description
            mycare.save()
            subject = 'Registration Successfull'
            message = f'Hii {mycare.name} you have registered successfully'
            email_from = settings.EMAIL_HOST_USER
            recipient_list=[mycare.email]
            send_mail(subject, message ,email_from,recipient_list)
            return render(request,'success.html')

def adminlogin(request):
    return render(request,'admin/sign-in.html')

class adminloginfunc(View):
    def post(self,request):
        email=request.POST['email']
        password=request.POST['password']
        check=P_admin.objects.filter(email=email,password=password)
        if check:
            return render(request,'admin/adminindex.html')
        else:
            return render(request,'admin/sign-in.html')

def candidates(request):
    return render(request,'admin/candidates.html')

class newSignUps(View):
    def get(self,request):
        query=P_user.objects.all()
        return render(request,'admin/candidates.html',{'query':query})

class movecandidate(View):
    def get(self,request,pk):
        if request.is_ajax():
            query1=P_user.objects.get(pk=pk)
            return JsonResponse({"message":"success"})
        return JsonResponse({"message":"wrong route"})

class index1(View):
    def get(self,request):
        return render(request,'index1.html')
        



    
     












