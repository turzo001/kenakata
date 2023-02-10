from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, Orderplaced


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
    


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',
        {'product':product})

def add_to_cart(request):
    return render(request, 'app/addtocart.html')

def buy_now(request):
    return render(request, 'app/buynow.html')

def profile(request):
    return render(request, 'app/profile.html')

def address(request):
    return render(request, 'app/address.html')

def orders(request):
    return render(request, 'app/orders.html')

def change_password(request):
    return render(request, 'app/changepassword.html')

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

def login(request):
    return render(request, 'app/login.html')

def customerregistration(request):
    return render(request, 'app/customerregistration.html')

def checkout(request):
    return render(request, 'app/checkout.html')

