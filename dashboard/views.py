from django.shortcuts import render,redirect

from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django.views import View

from app.models import Product,Customer,Orderplaced
from dashboard.forms import Productform,CustomerDetails,OrderplacedForm
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


# def ecommercecustomers(request):
#     return render(request,'dashboard/ecommerce-customers.html')
    
def ecommerceorderdetails(request):
    return render(request,'dashboard/ecommerce-customer-details.html')

def ecommerceorderdetails(request):
    return render(request,'dashboard/ecommerce-order-details.html')

# def ecommerceorders(request):
#     return render(request,'dashboard/ecommerce-orders.html')

class ProductListView(TemplateView):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.user_type=='developer':
                products=Product.objects.all().order_by('-id')
                count= Product.objects.count()
                context= {
                    'products':products,
                    'count':count
                    
                }
                return render(request,'dashboard/ecommerce-products.html',context)
            else:
                return redirect('index')
        else:
            return redirect('index')

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
        else:
            return redirect('ecommerceprod')
   
   
class ProductEditView(TemplateView):
    def get(self,request,pk,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.user_type=='developer':
                edit=Product.objects.get(pk=pk)
                form=Productform(instance=edit)
                context= {
                    'form':form,
                }
                return render(request,'dashboard/ecommerceaddproduct.html',context)
            else:
                return redirect('index')
        else:
            return redirect('index')
    def post(self,request,pk,*args,**kwargs):
        if request.user.user_type=='developer':
            if request.method=='post' or request.method=='POST':
                edit=Product.objects.get(pk=pk)
                form=Productform(request.POST,request.FILES,instance=edit)
                if form.is_valid():
                    form.save()
                    return redirect('ecommerceprod')
            else:
                return redirect('ecommerceprod')       
        else:
            return redirect('ecommerceprod')

    
class ecommerceorder(TemplateView):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.user_type=='developer':
                orders=Orderplaced.objects.all()
                count= Customer.objects.count()
                context= {
                    'orders':orders,
                    'count':count
                    
                }
                return render(request,'dashboard/ecommerceorders.html',context)
            else:
                return redirect('index')
        else:
            return redirect('index')
class OrderPlaced(TemplateView):
    def get(self,request,pk,*args,**kwargs):

        if request.user.is_authenticated:
            if request.user.user_type=='developer':
                order=Orderplaced.objects.get(pk=pk)
                form= OrderplacedForm(instance=order)
                
                context= {
                    'form':form
                }
                return render(request,'dashboard/ecommerce-order-details.html',context)
            else:
                return redirect('ecommerceorders')
            
        else:
            return redirect('index')

    
    def post(self,request,pk,*args,**kwargs):
        if request.user.user_type=='developer':
            if request.method=='post' or request.method=='POST':
                order=Orderplaced.objects.get(pk=pk)
                form=OrderplacedForm(request.POST,request.FILES,instance=order)
                if form.is_valid():
                    form.save()
                    return redirect('ecommerceorders')
            else:
                return redirect('ecommerceorders')       
        else:
            return redirect('ecommerceorders')
        
class ecommercecustomers(TemplateView):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.user_type=='developer':

                customer=Customer.objects.all()
                count= Customer.objects.count()
                context= {
                    'customer':customer,
                    'count':count
                    
                }
                return render(request,'dashboard/ecommerce-customers.html',context)
            else:
                return redirect('index')

        else:
            return redirect('index')
   
class ecommercecustomerdetails(TemplateView):
    def get(self,request,pk,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.user_type=='developer':

                customer=Customer.objects.get(pk=pk)
                form= CustomerDetails(instance=customer)
                context= {
                    'form':form    
                }
                return render(request,'dashboard/ecommerce-customer-details.html',context)
            else:
                return redirect('ecommercecustomers')
        return redirect('ecommercecustomers')

    def post(self,request,pk,*args,**kwargs):
        if request.user.user_type=='developer':
            if request.method=='post' or request.method=='POST':
                customer=Customer.objects.get(pk=pk)
                form=CustomerDetails(request.POST,request.FILES,instance=customer)
                if form.is_valid():
                    form.save()
                    return redirect('ecommercecustomers')
            else:
                return redirect('ecommercecustomers')       
        else:
            return redirect('ecommercecustomers')

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
        orders=Orderplaced.objects.all()
        count= Customer.objects.count()
        context= {
            'orders':orders,
            'count':count
            
        }
        return render(request,'dashboard/index.html',context)
    
    def post(self,request,*args,**kwargs):
        pass
    
    
# class ecommerceorder(TemplateView):
#     def get(self,request,*args,**kwargs):
#         if request.user.is_authenticated:
#             if request.user.user_type=='developer':
#                 orders=Orderplaced.objects.all()
#                 count= Customer.objects.count()
#                 context= {
#                     'orders':orders,
#                     'count':count
                    
#                 }
#                 return render(request,'dashboard/ecommerceorders.html',context)
#             else:
#                 return redirect('index')
#         else:
#             return redirect('index')

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
                                            
                                            ##reminder if i need multiple pk,so i will use different name in get or post like pk,fk 
