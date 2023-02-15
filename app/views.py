from django.shortcuts import render,redirect
from django.views import View
from .models import Customer, Product, Cart, Orderplaced
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwears= Product.objects.filter(catagory='TW')
        bottomwears= Product.objects.filter(catagory='BW')
        mobiles= Product.objects.filter(catagory='M')
        laptop= Product.objects.filter(catagory='L')
        return render(request, 'app/home.html',
        {'topwears':topwears,
        'laptop':laptop,
        'bottomwears':bottomwears,
        'mobiles':mobiles})
    
class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',
        {'product':product})

def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product= Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user == user]
        
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.discounted_price)
                amount += tempamount
                totalamount= amount + shipping_amount
            return render(request,'app/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})
        else:
            return render(request, 'app/emptycart.html')

def buy_now(request):
    return render(request, 'app/buynow.html')

def address(request):
    add= Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def orders(request):
    return render(request, 'app/orders.html')

def topwear(request,data=None):
    if data == None:
        topwears=Product.objects.filter(catagory='TW')
    elif data== 'below' :
        topwears=Product.objects.filter(catagory='TW').filter(discounted_price__lt=6000)
    elif data== 'above' :
        topwears=Product.objects.filter(catagory='TW').filter(discounted_price__gt=6000)
    elif data == 'yellow' or 'sara' or 'lee':
        topwears=Product.objects.filter(catagory='TW').filter(brand=data)
    return render(request, 'app/topwear.html',{'topwears':topwears})

def laptop(request,data=None):
    if data == None:
        laptops=Product.objects.filter(catagory='L')
    elif data== 'below' :
        laptops=Product.objects.filter(catagory='L').filter(discounted_price__lt=60000)
    elif data== 'above' :
        laptops=Product.objects.filter(catagory='L').filter(discounted_price__gt=60000)
    elif data == 'apple' or 'dell':
        laptops=Product.objects.filter(catagory='L').filter(brand=data)
    return render(request, 'app/laptop.html',{'laptops':laptops})

def bottomwear(request,data=None):
    if data == None:
        bottomwears=Product.objects.filter(catagory='BW')
    elif data== 'below' :
        bottomwears=Product.objects.filter(catagory='BW').filter(discounted_price__lt=1000)
    elif data== 'above' :
        bottomwears=Product.objects.filter(catagory='BW').filter(discounted_price__gt=1000)
    elif data == 'yellow' or 'lee':
        bottomwears=Product.objects.filter(catagory='BW').filter(brand=data)
    return render(request, 'app/bottomwear.html',{'bottomwears':bottomwears})

def mobile(request, data=None):
    if data == None:
        mobiles=Product.objects.filter(catagory='M')
    elif data== 'below' :
        mobiles=Product.objects.filter(catagory='M').filter(discounted_price__lt=120000)
    elif data== 'above' :
        mobiles=Product.objects.filter(catagory='M').filter(discounted_price__gt=120000)
    elif data == 'Redmi' or 'Samsung' or 'Apple':
        mobiles=Product.objects.filter(catagory='M').filter(brand=data)
#### if i'm using elif for below and above , then filter is not working, so i have used it after first if. surprisingly it's working then. ####

#here(if) also works,but if i'm using elif ,then not working
    # if data== 'below' :
    #     mobiles=Product.objects.filter(catagory='M').filter(discounted_price__lt=120000)
    # if data== 'above' :
    #     mobiles=Product.objects.filter(catagory='M').filter(discounted_price__gt=120000)
    return render(request, 'app/mobile.html',{'mobiles':mobiles})

class CustomerRegistrationView(View):
    def get(self,request):
        form= CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',
                      {'form':form})
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html',
                      {'form':form}) 
def checkout(request):
    return render(request, 'app/checkout.html')

class ProfileView(View):
    def get(self,request):
        form= CustomerProfileForm()
        return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request, 'congratulations profile updated successfully!!')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})

