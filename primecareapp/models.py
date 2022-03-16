from django.db import models

# Create your models here.

class P_Photo(models.Model):
    id=models.AutoField(primary_key=True)
    Photo=models.ImageField(upload_to='photo',default='',null=True)

# class P_Vaccination_certificate(models.Model):
#     id=models.AutoField(primary_key=True)
#     Certificate=models.FileField(upload_to='vaccine-certificate',default='',null=True)

class P_Work_permit_certificate(models.Model):
    id=models.AutoField(primary_key=True)
    passport=models.FileField(upload_to='passport',default='',null=True)
    visa=models.FileField(upload_to='visa',default='',null=True)
    brp=models.FileField(upload_to='brp',default='',null=True)
    passport_expiry_date=models.DateField(null=True,blank=True)
    visa_expiry_date=models.DateField(null=True,blank=True)
    brp_expiry_date=models.DateField(null=True,blank=True)

class P_previous_employer(models.Model):
    id=models.AutoField(primary_key=True)
    employername1=models.CharField(max_length=100,default='',null=True, blank=True)
    telenum1=models.CharField(max_length=100,default='',null=True, blank=True)
    employermail1=models.CharField(max_length=100,default='',null=True, blank=True)
    address1=models.CharField(max_length=100,default='',null=True, blank=True)
    employername2=models.CharField(max_length=100,default='',null=True, blank=True)
    telenum2=models.CharField(max_length=100,default='',null=True, blank=True)
    employermail2=models.CharField(max_length=100,default='',null=True, blank=True)
    address2=models.CharField(max_length=100,default='',null=True, blank=True)
    payslip1=models.FileField(upload_to='payslip1',default='',null=True, blank=True)
    payslip2=models.FileField(upload_to='payslip2',default='',null=True,blank=True)


class P_Address(models.Model):
    id=models.AutoField(primary_key=True)
    Proof=models.FileField(upload_to='address-proof',default='',null=True)

class P_Insurance(models.Model):
    id=models.AutoField(primary_key=True)
    Insurance=models.FileField(upload_to='insurance',default='',null=True)
    expiry_date=models.DateField(null=True,blank=True)
    
class P_Sssc(models.Model):
    id=models.AutoField(primary_key=True)
    certificate=models.FileField(upload_to='sssc',default='', null=True, blank=True)
    expiry_date=models.DateField(null=True,blank=True)

class P_Pvg(models.Model):
    id=models.AutoField(primary_key=True)
    pvg=models.FileField(upload_to='pvg',default='',null=True)
    pvgno=models.CharField(max_length=100,default='')

# class P_Qualification(models.Model):
#     id=models.AutoField(primary_key=True)
#     qualification=models.FileField(upload_to='qualification',default='',null=True)

class P_CV(models.Model):
    id=models.AutoField(primary_key=True)
    cv=models.FileField(upload_to='qualification',default='',null=True)

# class P_Handbook(models.Model):
#     id=models.AutoField(primary_key=True)
#     Handbook=models.FileField(upload_to='handbook',default='',null=True)

# class P_Contract(models.Model):
#     id=models.AutoField(primary_key=True)
#     Contract=models.FileField(upload_to='contract',default='',null=True)
#     expiry_date=models.DateField()

class P_Experience(models.Model):
    id=models.AutoField(primary_key=True)
    ManualHandling=models.FileField(upload_to='ManualHandling',default='',null=True)
    FireSafety=models.FileField(upload_to='FireSafety',default='',null=True)
    HealthSafety=models.FileField(upload_to='HealthSafety',default='',null=True)
    InfectionControl=models.FileField(upload_to='ManualHandling',default='',null=True)

class P_user(models.Model):
    id=models.AutoField(primary_key=True)
    # select=models.CharField(max_length=100,default='')
    Firstname=models.CharField(max_length=100,default='')
    Lastname=models.CharField(max_length=100,default='')
    PhoneNumber=models.CharField(max_length=100,default='')
    Date_of_birth=models.DateField(null=True, blank=True)
    Email=models.CharField(max_length=100,default='')
    Password=models.CharField(max_length=100,default='')
    Address_1=models.CharField(max_length=100,default='')
    Address_2=models.CharField(max_length=100,default='')
    Address_3=models.CharField(max_length=100,default='',null=True)
    postcode=models.CharField(max_length=100,default='')
    otp=models.CharField(max_length=100,default='')
    SortCode=models.CharField(max_length=100,default='')
    Photo_id=models.ForeignKey(P_Photo,on_delete=models.CASCADE,null=True)
    vaccine1=models.DateField(null=True,blank=True)
    vaccine2=models.DateField(null=True,blank=True)
    booster=models.DateField(null=True,blank=True)
    Previous_id=models.ForeignKey(P_previous_employer,on_delete=models.CASCADE,null=True)
    workpermit_id=models.ForeignKey(P_Work_permit_certificate,on_delete=models.CASCADE,null=True)
    Address_id=models.ForeignKey(P_Address,on_delete=models.CASCADE,null=True)
    Sssc_id=models.ForeignKey(P_Sssc,on_delete=models.CASCADE,null=True)
    skills=models.CharField(max_length=100,default='',null=True)
    Pvg_id=models.ForeignKey(P_Pvg,on_delete=models.CASCADE,null=True)
    Cv_id=models.ForeignKey(P_CV,on_delete=models.CASCADE,null=True)
    Experience_id=models.ForeignKey(P_Experience,on_delete=models.CASCADE,null=True)
    AccountNo=models.CharField(max_length=100,default='',null=True)
    NInumber=models.CharField(max_length=100,default='',null=True)
    status=models.CharField(max_length=100,default='',null=True)

    def __str__(self):
        return "{}:{}".format(str(self.id), str(self.Firstname))

# class P_details(models.Model):
#     SortCode=models.CharField(max_length=100,default='')
#     User_id=models.ForeignKey(P_user,on_delete=models.CASCADE,null=True)
#     Photo_id=models.ForeignKey(P_Photo,on_delete=models.CASCADE,null=True)
#     Covidteststatus=models.CharField(max_length=100,default='')
#     Covid_test_expire_date=models.DateField(null=True, blank=True)
#     Vaccination_id=models.ForeignKey(P_Vaccination_certificate,on_delete=models.CASCADE,null=True)
#     Workpermit_id=models.ForeignKey(P_Work_permit_certificate,on_delete=models.CASCADE,null=True)
#     Address_id=models.ForeignKey(P_Address,on_delete=models.CASCADE,null=True)
#     Insurance_id=models.ForeignKey(P_Insurance,on_delete=models.CASCADE,null=True)
#     Sssc_id=models.ForeignKey(P_Sssc,on_delete=models.CASCADE,null=True)
#     skills=models.CharField(max_length=100,default='')
#     Pvg_id=models.ForeignKey(P_Pvg,on_delete=models.CASCADE,null=True)
#     Qualification_id=models.ForeignKey(P_Qualification,on_delete=models.CASCADE,null=True)
#     Handbook_id=models.ForeignKey(P_Handbook,on_delete=models.CASCADE,null=True)
#     Contract_id=models.ForeignKey(P_Contract,on_delete=models.CASCADE,null=True)
#     Experience_id=models.ForeignKey(P_Experience,on_delete=models.CASCADE,null=True)
#     toc=models.CharField(max_length=100,default='')

class P_Contact(models.Model):
    Name=models.CharField(max_length=100,default='')
    Subject=models.CharField(max_length=100,default='')
    Email=models.CharField(max_length=100,default='')
    Message=models.CharField(max_length=100,default='')
    def __str__(self):
        return self.Name

# class P_Contacts(models.Model):
#     Name=models.CharField(max_length=100,default='')
#     Email=models.CharField(max_length=100,default='')
#     Message=models.CharField(max_length=100,default='')
#     def __str__(self):
#         return self.Name

class user_temp(models.Model):
    id=models.AutoField(primary_key=True)
    select=models.CharField(max_length=100,default='')
    Firstname=models.CharField(max_length=100,default='')
    Lastname=models.CharField(max_length=100,default='')
    PhoneNumber=models.CharField(max_length=100,default='')
    Date_of_birth=models.DateField(null=True, blank=True)
    Email=models.CharField(max_length=100,default='')
    Password=models.CharField(max_length=100,default='')
    Address_1=models.CharField(max_length=100,default='')
    Address_2=models.CharField(max_length=100,default='')
    Address_3=models.CharField(max_length=100,default='')
    postcode=models.CharField(max_length=100,default='')
    otp=models.CharField(max_length=100,default='')

class P_caretaker(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    phonenumber=models.CharField(max_length=100,default='')
    description=models.CharField(max_length=100,default='')

class P_admin(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=100,default='')
    password=models.CharField(max_length=100,default='')









 
