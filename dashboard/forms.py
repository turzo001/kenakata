from django.forms.models import ModelForm
from app.models import CATAGORY_CHOICES,Product,Orderplaced,Customer
from account.models import User
from django import forms

# class Productform(forms.ModelForm):
#     class Meta:
#         model=Product
#         fields=('__all__')
#         widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
#                  'selling_price':forms.FloatField(attrs={'class':'form-control'}),
#                  'discounted_price':forms.FloatField(attrs={'class':'form-control'}),
#                  'description':forms.TextInput(attrs={'class':'form-control'}),
#                  'brand':forms.CharField(attrs={'class':'form-control'}),
#                  'catagory':forms.CharField(attrs={'class':'form-control'}),
#                  'product_image':forms.ImageField(attrs={'class':'form-control'})
            
#         }
        
class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields= ['title','selling_price','discounted_price','description','brand','catagory','product_image']
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'selling_price':forms.NumberInput(attrs={'class':'form-control'}),
                 'discounted_price':forms.NumberInput(attrs={'class':'form-control'}),
                 'description':forms.TextInput(attrs={'class':'form-control'}),
                 'brand':forms.TextInput(attrs={'class':'form-control'}),
                 'catagory':forms.TextInput(attrs={'class':'form-control'})
                 }
class OrderplacedForm(forms.ModelForm):
    class Meta:
        model=Orderplaced
        fields='__all__'
        widgets={
            'user':forms.TextInput(attrs={'class':'form-control'}),
            'customer':forms.TextInput(attrs={'class':'form-control'}),
            'product':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.TextInput(attrs={'class':'form-control'}),
            'ordered_date':forms.NumberInput(attrs={'class':'form-control'}),
            
            }
        

class CustomerDetails(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        widgets={
            'user':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'})
            }
