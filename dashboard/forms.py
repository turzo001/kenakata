from django.forms.models import ModelForm
from app.models import CATAGORY_CHOICES,Product
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
                #  'selling_price':forms.IntegerField(attrs={'class':'form-control'}),
                #  'discounted_price':forms.IntegerField(attrs={'class':'form-control'}),
                 'description':forms.TextInput(attrs={'class':'form-control'}),
                 'brand':forms.TextInput(attrs={'class':'form-control'})
                #  'catagory':forms.TextInput(attrs={'class':'form-control'})
                 }
    