from django.urls import path,re_path
# from primecareapp import views
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from .views import staff_register,candidate1,Staff_reg_func,userList,admin_logout,locations,index,updateprofile,list1,contactList,otp_cnfrm,contact,file_upload,care_reg,care_reg_func,adminlogin,adminloginfunc,adminindex,newSignUps,movecandidate,index1

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
    path('adminindex/', adminindex),
    path('newSignUps/', newSignUps.as_view()),
    path('movecandidate/', movecandidate.as_view()),
    path('index1/', index1.as_view()),
    path('list1/', list1.as_view()),
    path('updateprofile/', updateprofile.as_view()),
    path('candidate1/', candidate1.as_view()),
    path('admin_logout/', admin_logout),
    # path('getcandidate/', getcandidate.as_view()),
    path('locations/', locations.as_view()),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)