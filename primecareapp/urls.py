from django.urls import path,re_path
# from primecareapp import views
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
# from django.conf.urls import url

from .views import staff_register,Staff_reg_func,userList,index,contactList,otp_cnfrm,contact,file_upload,care_reg,care_reg_func,adminlogin,adminloginfunc,candidates,newSignUps,movecandidate,index1

urlpatterns = [
    path('', index),
    
    path('staff_register/',staff_register),
    path('staff_reg_func/',Staff_reg_func.as_view()),
    path('users/',userList.as_view()),
    path('contacts/',contactList.as_view()),
    # path('api/', Api.as_view(), name='api'),
    re_path(r'^contact/',contact.as_view()),
    # path('staff_html/',staff_html),
    path('otp_cnfrm/',otp_cnfrm.as_view()),
    path('file_upload/',file_upload.as_view()),
    path('care_reg/',care_reg.as_view()),
    path('care_reg_func/',care_reg_func.as_view()),
    path('care_reg_func/',care_reg_func.as_view()),
    path('adminloginfunc/', adminloginfunc.as_view()),
    path('adminlogin/', adminlogin),
    path('candidates/', candidates),
    path('newSignUps/', newSignUps.as_view()),
    path('movecandidate/<int:pk>', movecandidate.as_view()),
    path('index1/', index1.as_view()),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]