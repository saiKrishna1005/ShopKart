from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path("productlist/",productlistpage.as_view(),name='productlist'),
    path("userlist/",userlistpage.as_view(),name='userlist'),
    path("product/",productaddpage.as_view(),name="product"),
    path("productlist/update/<int:id>/",updatedata.as_view(),name="update"),
    path("productlist/delete/<int:id>/",deletedata.as_view(),name="delete"),
    path("adminhome/",adminhomepage.as_view(),name="adminhome"),
    path('adminlogin/', adminloginpage.as_view()),



    ]
