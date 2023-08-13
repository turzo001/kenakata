from django.shortcuts import render,redirect

from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django.views import View

from app.models import Product
from dashboard.forms import Productform
# from dashboard.forms import Productform



#                        ############ dashboard ###### 

def basiclogin(request):
    return render(request,'dashboard/auth-basic-login.html')

def basicregister(request):
    return render(request,'dashboard/auth-basic-register.html')

def basicresetpass(request):
    return render(request,'dashboard/auth-basic-reset-password.html')

def basicforgotpass(request):
    return render(request,'dashboard/auth-basic-forgot-password.html')



def ecommercecustomerdetails(request):
    return render(request,'dashboard/ecommerce-customer-details.html')

def ecommercecustomers(request):
    return render(request,'dashboard/ecommerce-customers.html')
    
def ecommerceorderdetails(request):
    return render(request,'dashboard/ecommerce-customer-details.html')

def ecommerceorderdetails(request):
    return render(request,'dashboard/ecommerce-order-details.html')

def ecommerceorders(request):
    return render(request,'dashboard/ecommerce-orders.html')

class ProductListView(TemplateView):
    def get(self,request,*args,**kwargs):
        products=Product.objects.all().order_by('-id')
        count= Product.objects.count()
        context= {
            'products':products,
            'count':count
            
        }
        return render(request,'dashboard/ecommerce-products.html',context)

    def post(self,request,*args,**kwargs):
        pass

class AddProduct(TemplateView):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.user_type=='developer':
                form=Productform()
                context= {
                    'form':form
                }
                return render(request,'dashboard/ecommerceaddproduct.html',context)
            else:
                return redirect('ecommerceprod')
        return redirect('ecommerceprod')
    
    def post(self,request,*args,**kwargs):
        if request.user.user_type=='developer':
            if request.method=='post' or request.method=='POST':
                form=Productform(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('addnewprod')
            else:
                return redirect('ecommerceprod')       
        else:
            return redirect('ecommerceprod')
        
class ProductEditView(TemplateView):
    def get(self,request,pk,*args,**kwargs):
        edit=Product.objects.get(pk=pk)
        form=Productform(instance=edit)
        context= {
            'form':form,
        }
        return render(request,'dashboard/ecommerceaddproduct.html',context)

class ProductDeleteView(DeleteView):
    # model= Product
    # success_url = 'dashboard:ecommerceprod'
    def get(self,request,pk,*args,**kwargs):
        edit=Product.objects.get(pk=pk)
        edit.delete()
        return redirect('ecommerceprod')

# class ProductEditView(View):
#     def get(self,request,pk):
#         products=Product.objects.get(pk=pk)
#         return render(request, 'dashboard:ecommerceaddproduct.html',{'products':products})

class dashboardindex(TemplateView):
    def get(self,request,*args,**kwargs):
        return render(request,'dashboard/index.html')

    def post(self,request,*args,**kwargs):
        pass
    

def pageseditprofile(request):
    return render(request,'dashboard/pages-edit-profile.html')


def pageseror403(request):
    return render(request,'dashboard/pages-error-403.html')

def pageseror404(request):
    return render(request,'dashboard/pages-error-404.html')
    
def pageseror500(request):
    return render(request,'dashboard/pages-error-500.html')

def pricingtable(request):
    return render(request,'dashboard/pricing-table.html')

def timeline(request):
    return render(request,'dashboard/timeline.html')

def userprofile(request):
    return render(request,'dashboard/user-profile.html')

#                        ############ dashboard ###### 
                                            ##### boxed or cover authentication #####
