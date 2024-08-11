from django.shortcuts import render,redirect
from Shop.form import *
from Shop.models import *
from .form import*
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User




# Create your views here.
class adminloginpage(APIView):
    
    def get(self,request):
    
        msg={
            "error":""
        }
    
        return render(request,'shop/admin_login.html',msg)


    def post(self,request):            
        user=authenticate(username=request.POST['username'],
                        password=request.POST['password'])
        if user is not None:
            loggedUser=User.objects.get(username=user)
            if loggedUser.is_staff:

                login(request,user)
            
                return redirect('/Admin/adminhome/')
            else:
                msg={
                    "error":"**you are not admin"
                }
                return render(request,"shop/admin_login.html",msg)
        
        else:
            msg={
                "error":"**Invalid username or Password"
            }
            return render(request,"shop/admin_login.html",msg)
                

class adminhomepage(APIView):

    def get(self,request):
        return render(request,"shop/adminhome.html")  

class productaddpage(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
    

    def get(self,request):

        data ={
            "productform":Product_Form()
           }
        return render(request,'shop/product.html',data)

    def post(self,request):
        hello = Product_Form(request.POST)
        if hello.is_valid():
            hello.save()
            return redirect("/Admin/productlist/")
        
class productlistpage(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
    def get(self,request):
      
        data = {
            "list":Product.objects.all()
            }
        return render(request,'shop/productlist.html',data)
    
class userlistpage(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
    
    
    def get(self,request):
      
        data = {
            "list":User.objects.all()
            }
        return render(request,'shop/userlist.html',data)
    
class updatedata(APIView):
    def get(self,request,id):
        update_row=Product.objects.get(id=id) #deletedata
    
        data ={
            "productform":Product_Form(instance=update_row)
           }
    
        return render(request,'shop/product.html',data)

    def post(self,request,id):
        update_row=Product.objects.get(id=id) #deletedata
        hello = Product_Form(request.POST,instance=update_row)
        if hello.is_valid():
            hello.save()
            return redirect('/Admin/productlist/')
        
class deletedata(APIView):
    def get(self,request,id):
        selected_row=Product.objects.get(id=id)
        selected_row.delete()

        return redirect('/Admin/productlist/')
    
