from django import forms
from Shop.models import *

class Product_Form(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        widgets={

            "name":forms.TextInput(attrs={"class":"form-control shadow p-1 mb-2 bg-body rounded-3 border border-info border-3"}),
            "vendor":forms.TextInput(attrs={"class":"form-control shadow p-1 mb-2 bg-body rounded-3 border border-info border-3"}),
            "product_image":forms.FileInput(attrs={"class":"form-control"}),
            "quantity":forms.NumberInput(attrs={"class":"form-control shadow p-1 mb-2 bg-body rounded-3 border border-info border-3"}),



            "original_price":forms.NumberInput(attrs={"class":"form-control shadow p-1 mb-2 bg-body rounded-3 border border-info border-3"}),
            "selling_price":forms.NumberInput(attrs={"class":"form-control shadow p-1 mb-2 bg-body rounded-3 border border-info border-3"}),
            "description":forms.TextInput(attrs={"class":"form-control shadow p-1 mb-2 bg-body rounded-3 border border-info border-3"}),
            
        }

        

